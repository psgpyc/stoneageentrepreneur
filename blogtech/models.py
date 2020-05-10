from django.db import models
from blogtech.abstractModels import TimeStampModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Tags(TimeStampModel):

    name = models.CharField(max_length=100, unique=True)
    slug_name = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)


class BlogCategory(TimeStampModel):

    name = models.CharField(max_length=100, verbose_name='Blog Categories')

    slug_name = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Main Blog Category'
        verbose_name_plural = 'Main Blog categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)


class PostCategory(TimeStampModel):

    belongs_to = models.ForeignKey(BlogCategory,
                                   on_delete=models.DO_NOTHING,
                                   related_name='blogposts',
                                   related_query_name='blogpost')
    name = models.CharField(max_length=50, verbose_name='Post Category Name')
    tags = models.ManyToManyField(Tags,
                                  related_name='posts',
                                  related_query_name='post'
                                  )
    slug_name = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Blog Post Category'
        verbose_name_plural = 'Blog Post Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(PostCategory, self).save(*args, **kwargs)


class Comment(TimeStampModel):
    comment = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment[10]


def image_upload_path(instance, file_name):
    return '{}/{}/{}'.format(instance.created_on, instance.created_by, file_name)


class Post(TimeStampModel):
    belongs_to = models.ManyToManyField(PostCategory)
    has_tags = models.ManyToManyField(Tags)
    hard_title = models.CharField(max_length=100)
    soft_title = models.CharField(max_length=50)
    title_image = models.ImageField(upload_to=image_upload_path)
    post_body = models.TextField()
    comments = models.ManyToManyField(Comment)
    flags = models.PositiveIntegerField()
    # flag:1-3 - featured  flag:5-10 - picks
    slug_name = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Blog Post '
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.hard_title

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.hard_title)
        super(Post, self).save(*args, **kwargs)


def subpostcontentimage(instance,file_name):
    return '{}/{}/{}'.format(instance.created_on, instance.created_by, file_name)


class SubPostContent(TimeStampModel):
    belongs_to = models.ForeignKey(Post, on_delete=models.CASCADE)
    inter_post_heading = models.CharField(max_length=100)
    inter_post_content = models.TextField()
    highlight_content = models.TextField()
    post_image = models.ImageField(upload_to=subpostcontentimage)

    class Meta:
        verbose_name = 'Blog Post Heading '
        verbose_name_plural = 'Blog Posts Headings'

    def __str__(self):
        return self.inter_post_heading[10]





