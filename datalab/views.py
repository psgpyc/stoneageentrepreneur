from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from datalab.models import SharePost, PostComment
from django.views.generic import TemplateView
from .forms import SharePostForm, CommentPostForm
from django.views import View
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
from .utils import get_json_ready


class Home(LoginRequiredMixin,TemplateView):
    template_name = 'datalab/log-index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        posts = SharePost.objects.filter(is_active=True)
        context['posts'] = posts
        context['postform'] = SharePostForm()
        context['commentForm'] = CommentPostForm()

        return context


class PostUpdate(View):

    def post(self, request):
        user = request.user
        form = SharePostForm(request.POST)
        codeLen = len(request.POST.get('code', None))
        if request.is_ajax:
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.created_by = user
                if codeLen != 0:
                    model_instance.code = highlight(form.cleaned_data['code'], PythonLexer(), HtmlFormatter(style='native'))
                model_instance.save()
                posted = True
            else:
                posted = False

            data = {
                'registered': posted,
                'messages': 'content is posted'
            }

            return JsonResponse(data)

        return render(request, template_name='datalab/log-index.html', context={})


class AddComments(View):

    def post(self, request):
        user = request.user
        ppid = SharePost.objects.get(id=request.POST.get('postid'))
        form = CommentPostForm(request.POST)

        if request.is_ajax:
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.created_by = user
                model_instance.belongs_to = ppid

                model_instance.save()
                posted = True

            data = {
                'posted': 'the comment has been posted',

            }

            return JsonResponse(data)

        return render(request, template_name='datalab/log-index.html', context={})


class GetComments(View):

    def get(self, request):
        data = {'comments': []}

        post_id = int(request.GET.get('postId',None))
        if post_id is not None and type(post_id) == int:
            if request.is_ajax:
                data['comments'].append(get_json_ready(model_instance=SharePost.objects.get_comments(post_id)[0]))
                data['comments'].append(get_json_ready(model_instance=SharePost.objects.get_comments(post_id)[1]))
                data['comments'].append(get_json_ready(model_instance=SharePost.objects.get_comments(post_id)[3]))
                data['comments'].append(get_json_ready(model_instance=SharePost.objects.get_comments(post_id)[4]))
                print(data)
                return JsonResponse(data)

        return render(request, template_name='datalab/log-index.html', context={})