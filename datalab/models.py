from django.db import models
from blog.abstractModels import TimeStampModel
from markdown import markdown


class PostManager(models.Manager):

    def get_comments(self, instance):
        return self.filter(id=instance).prefetch_related('post_comments')[0].post_comments.select_related(
            'created_by').all()


class SharePost(TimeStampModel):
    content = models.TextField()
    code = models.TextField(blank=True, null=True)

    objects = PostManager()

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-created_on',]


class PostComment(TimeStampModel):
    belongs_to = models.ForeignKey(SharePost, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.TextField()
    codeContent = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Comments by: {self.created_by}'


