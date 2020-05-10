from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'blogtech/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class Posts(TemplateView):
    template_name = 'blogtech/posts.html'

    def get_context_data(self, **kwargs):
        context = super(Posts, self).get_context_data(**kwargs)
        context['title'] = 'Posts'
        return context
