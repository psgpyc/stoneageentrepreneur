from django.contrib import admin
from blogtech.models import Tags,Post, PostCategory, SubPostContent, BlogCategory, Comment

admin.site.register(Tags)
admin.site.register(PostCategory)
admin.site.register(SubPostContent)
admin.site.register(BlogCategory)
admin.site.register(Comment)