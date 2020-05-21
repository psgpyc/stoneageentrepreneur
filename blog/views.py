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
            'featured_two': random.sample(tuple(query_set(2)), k=2),
            'featured_four': random.sample(tuple(query_set(5)), k=3),
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
        qs = BlogCategory.objects.per_category(self.kwargs['post_slug'])
        print(self.kwargs)

        ctx = {
            'blog_categories': qs,
            'the_featured_one': get_categories_featured(the_slug=self.kwargs['post_slug']),
            'whereiam': get_where_i_am(self.kwargs['post_slug'])

        }
        print(qs)
        print(len(connection.queries))

        return render(request, template_name=self.template_name, context=ctx)


class MiniCategories(TemplateView):
    template_name = 'blog/minicategories.html'

    def get_context_data(self, **kwargs):
        a=PostCategory.objects.filter(slug_name=self.kwargs['post_slug']).select_related('belongs_to')
        context = super(MiniCategories, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['post_slug']
        context['whereiam'] = get_where_i_am(self.kwargs['post_slug'])
        context['whereiwas'] = a[0].belongs_to
        return context
