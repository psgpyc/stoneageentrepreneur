from django.contrib import admin
from blog.models import Tags,Post, SubPostContent, BlogCategory, Comment, SubPostListElements, ListElements, PostCategory, SiteCategory

admin.site.register(Tags)
admin.site.register(SubPostContent)
admin.site.register(BlogCategory)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(SubPostListElements)
admin.site.register(ListElements)
admin.site.register(PostCategory)
admin.site.register(SiteCategory)
