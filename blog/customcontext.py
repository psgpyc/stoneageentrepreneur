from accounts.forms import UserLoginForm, RegistrationForm
from blog.models import BlogCategory, SiteCategory


def get_categories(request):
    qs = BlogCategory.objects.active()
    ctx = {
        'categories': qs,
        'form': UserLoginForm(),
        'regForm': RegistrationForm(),

    }
    return ctx
