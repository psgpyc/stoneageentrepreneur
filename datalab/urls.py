from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.conf import settings
from .views import Home, PostUpdate, AddComments, GetComments

urlpatterns = [
    path('', Home.as_view(), name='home-auth'),
    path('post/update/', PostUpdate.as_view(), name='post-update'),
    path('post/add-comment/', AddComments.as_view(), name='post-add-comment'),
    path('post/get-comments/', GetComments.as_view(), name='post-get-comments')

]