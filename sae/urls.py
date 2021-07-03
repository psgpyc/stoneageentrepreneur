from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from django.conf import settings
from django.contrib.auth import views as auth_views


from blog.views import HomePage, PostDetails, Categories, MiniCategories, RegistrationView, UserLogoutView, \
    AccountEmailActivate, UserPasswordResetComplete, SearchView, DataLiteracy
from accounts.forms import UserLoginForm, UserPasswordResetForm, UserPasswordResetConfirmForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', HomePage.as_view(), name='data-literacy-project'),

    path('', DataLiteracy.as_view(), name='home'),
    path('home/', include('datalab.urls'), name='home-auth-redirect'),

    path('posts/<slug:post_slug>/', PostDetails.as_view(), name='post-details'),
    path('categories/<slug:post_slug>', Categories.as_view(), name='categories'),
    path('mini/<slug:post_slug>', MiniCategories.as_view(), name='mini-categories'),

    path('ajax/search/', SearchView.as_view(), name='search-view'),

    path('data-literacy/', DataLiteracy.as_view(), name='data-literacy-project'),

    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
         template_name='blog/login.html',
         authentication_form=UserLoginForm), name='user-login'),
    path('register/', RegistrationView.as_view(), name='user-register'),

    path('logout/',
         login_required(UserLogoutView.as_view(template_name='blog/index.html', )),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='user-logout'),


    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
                AccountEmailActivate.as_view(),
                name='email-activate'),

    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='blog/password_reset_form.html',
             form_class=UserPasswordResetForm,
         ),

         name='password-reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='blog/password_reset_done.html'
         ),
         name='password_reset_done'),


    path('reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='blog/password_reset_confirm.html',
             form_class=UserPasswordResetConfirmForm,

         ),
         name='password_reset_confirm'),
    path('reset/complete/',
         UserPasswordResetComplete.as_view(
             template_name='blog/password_reset_complete.html',
         ),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)