from blog.models import Post, BlogCategory, PostCategory
from django.db.models import Prefetch
import random


def update_featured_flag():
    """
    A Celery dependent async method to update
    featured falg to initila after defined period
    in settings.py

    :return:
    """
    a_featured = Post.objects.get(id=2)
    a_featured.flags = 0
    a_featured.save()


def get_where_i_am(title):
    """
    A python split and join implementation
    to generate walk-through title

    :param title: slug url from request.kwargs
    :return: split and joined slug
    """
    title = title.split('-')
    whereiam = ' '.join(title)
    return whereiam


def get_categories_featured(the_slug):
    """
    A Postgres dependent ORM filter to get
    posts related to categories and active flag
    :param the_slug:
    :return: a random post from a python list with active flags
    """
    featured_list = []
    featured = BlogCategory.objects.prefetch_related(
        Prefetch('postcategory_set', queryset=PostCategory.objects.prefetch_related(
            Prefetch('post_set', queryset=Post.objects.filter(flags=41).prefetch_related('has_tags'))))).get(slug_name=the_slug)

    for featured_post_category in featured.postcategory_set.all():
        for featured_post in featured_post_category.post_set.all():
            featured_list.append(featured_post)
    if len(featured_list) == 0:
        return ''
    else:
        return random.choice(featured_list)
