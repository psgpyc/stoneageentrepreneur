from blog.models import Post


class CustomSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        print(request.path.split('/'))
        if request.path.split('/')[1] == 'posts':
            if 'has_viewed_post_{}'.format(view_kwargs['post_slug']) not in request.session:
                post = Post.objects.get(slug_name=view_kwargs['post_slug'])
                post.view_count += 1
                post.save()
                request.session['has_viewed_post_{}'.format(view_kwargs['post_slug'])] = True

        return None
