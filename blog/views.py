from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView, DetailView
from django.db.models import Prefetch
from blog.models import Post, SubPostContent, SubPostListElements, ListElements, BlogCategory, PostCategory
from django.db import connection, reset_queries
from blog.utils import get_where_i_am, get_categories_featured
import random


class HomePage(View):
    template_name = 'blog/index.html'

    def get(self, request):
        def query_set(flag): return Post.objects.featured_post(flag)
        ctx = {
            'featured_one': random.choice(query_set(1)),
            'featured_two': random.sample(tuple(query_set(2)), k=3),
            'all_posts': Post.objects.exclude(flags__gt=0),
            'title': 'HOME'
        }
        print(len(connection.queries))

        return render(request, template_name=self.template_name, context=ctx)


class PostDetails(DetailView):
    model = Post
    template_name = 'blog/posts.html'
    slug_field = 'slug_name'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data(**kwargs)
        context['title'] = self.object.hard_title
        return context

    def get_object(self, queryset=None):
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
        return post


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







