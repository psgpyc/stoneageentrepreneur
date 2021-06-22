from django.contrib.auth.views import LogoutView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.views.generic import View
from django.views.generic import TemplateView, DetailView
from django.db.models import Prefetch
from django.views.generic.edit import FormMixin

from accounts.models import ActivateEmail
from blog.models import Post, SubPostContent, SubPostListElements, ListElements, BlogCategory, PostCategory
from django.db import connection, reset_queries
from blog.utils import get_where_i_am, get_categories_featured
import random
from django.contrib import messages

from django.http import JsonResponse


from accounts.forms import UserLoginForm, RegistrationForm, ReactivateEmailForm

from django.contrib.sessions.models import Session


class HomePage(View):
    template_name = 'blog/index.html'

    def get(self, request):
        def query_set(flag): return Post.objects.featured_post(flag)
        ctx = {
            'form': UserLoginForm(),
            'regForm': RegistrationForm(),
            'featured_one': random.choice(query_set(1)),
            'featured_two': random.sample(tuple(query_set(2)), k=3),
            'all_posts': Post.objects.exclude(flags__gt=0),
            'title': 'HOME'
        }

        return render(request, template_name=self.template_name, context=ctx)


class PostDetails(View):
    template_name = 'blog/posts.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.prefetch_related(
            Prefetch('has_tags'),
            Prefetch(
                'subpostcontent_set',
                queryset=SubPostContent.objects.prefetch_related(
                    Prefetch(
                        'subpostlistelements_set',
                        queryset=SubPostListElements.objects.prefetch_related(
                            Prefetch(
                                'listelements_set')))))).get(slug_name=self.kwargs['post_slug'])
        ctx = {
            'title': post.hard_title,
            'post': post,
        }

        return render(request, template_name=self.template_name, context=ctx)


class Categories(View):
    template_name = 'blog/categories.html'

    def get(self, request, *args, **kwargs):
        active_category = BlogCategory.objects.filter(slug_name=self.kwargs['post_slug']).prefetch_related('postcategory_set')
        qs = Post.objects.exclude(flags=41).select_related('belongs_to').select_related('belongs_to').\
            filter(belongs_to__belongs_to__slug_name=self.kwargs['post_slug'])

        def query_set(flag): return Post.objects.featured_post(flag)

        ctx = {
            'active_category': active_category[0],
            'blog_categories': qs,
            'the_featured_one': get_categories_featured(the_slug=self.kwargs['post_slug']),
            'whereiam': get_where_i_am(self.kwargs['post_slug'])

        }
        print(len(connection.queries))

        return render(request, template_name=self.template_name, context=ctx)


class MiniCategories(View):
    template_name = 'blog/minicategories.html'

    def get(self, request, *args, **kwargs):
        qs = Post.objects.select_related(
            'belongs_to__belongs_to').\
            filter(
            belongs_to__slug_name=self.kwargs['post_slug']).\
            prefetch_related('has_tags')

        ctx = {
            'posts': qs,
            'whereiam': get_where_i_am(self.kwargs['post_slug']),
            'whereiwas': qs[0].belongs_to.belongs_to

        }

        return render(request, template_name=self.template_name, context=ctx)


class SearchView(View):
    def post(self, request, *args, **kwargs):
        result = []

        q = request.POST.get('query')
        search_qs = Post.objects.filter(hard_title__icontains=q)

        for eachPost in search_qs:
            result.append((eachPost.hard_title, eachPost.slug_name))

        if request.is_ajax():
            print(result)
            return JsonResponse({'data': result}, status=200)

        return render(request, template_name='blog/index.html', context={})


class Home(LoginRequiredMixin,TemplateView):
    template_name = 'blog/home.html'


class RegistrationView(View):
    template_name = 'blog/register.html'
    ctx = {
        'form': RegistrationForm(),
        'title': 'Register'
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, template_name=self.template_name, context=self.ctx)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('full_name')
            print(username)
            messages.success(request,
                             'Hey {} ! Your account has been registered. '
                             'Please check your email to activate your account.'.format(username))
            return redirect('user-register')

        return render(request, template_name=self.template_name,
                      context={'form': form, 'title': 'Registration'})


class UserLogoutView(LogoutView):
    def __init__(self, *args, **kwargs):
        super(UserLogoutView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserLoginForm()

        return context


class UserPasswordResetComplete(PasswordResetCompleteView):
    def __init__(self, *args, **kwargs):
        super(PasswordResetCompleteView, self).__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        super(PasswordResetCompleteView, self).__init__(*args, **kwargs)
        messages.success(request, 'You have successfully reset your password. '
                                  'Please Login to continue.')

        return redirect('/login/')


class AccountEmailActivate(FormMixin, View):
    form_class = ReactivateEmailForm
    success_url = '/reset/done/'

    def get(self, request, key, *args, **kwargs):
        qs = ActivateEmail.objects.filter(path_key__iexact=key)
        qs_confirm = qs.confirmable()
        if qs_confirm.count() == 1:
            obj = qs.first()
            obj.activate()
            messages.success(request, 'Your Email has been confirmed. '
                                      'You can now login to SAE using your email and password.')
            return redirect('user-login')
        else:
            qs_activated = qs.filter(activated=True)
            if qs_activated.exists():
                reset_link = reverse('password-reset')
                msg = """
                    You have already confirmed your Email address. In case you forget,
                    Do you want to <a href={}>reset your password?</a>
                """.format(reset_link)
                messages.success(request, mark_safe(msg))
                return redirect('user-login')
        ctx = {'form':self.get_form()}
        return render(request, template_name='blog/registration-error.html', context=ctx)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        msg = """
        Activation link has been sent to you, Please check your Email.
        """
        messages.success(self.request, msg)
        email = form.cleaned_data.get('email')
        obj = ActivateEmail.objects.email_exists(email).first()
        if obj.regenerate():
            obj.send_activation_email()
        return super(AccountEmailActivate, self).form_valid(form)

    def form_invalid(self, form):

        ctx = {'form': self.get_form()}
        return render(self.request, template_name='blog/registration-error.html', context=ctx)


class DataLiteracy(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, template_name='blog/data_literacy_project.html', context={'title': 'Data Literacy Project'})