from blog.models import BlogCategory


def get_categories(request):
    qs = BlogCategory.objects.active()
    ctx = {
        'categories': qs

    }
    return ctx
