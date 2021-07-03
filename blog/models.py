from datetime import timedelta

from django.conf import settings
from django.db import models
from django.db.models import Prefetch
from django.utils import timezone

from blog.abstractModels import TimeStampModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()

DEFAULT_FEATURE_DAYS = getattr(settings, 'DEFAULT_FEATURE_DAYS', 7)


class Tags(TimeStampModel):

    name = models.CharField(max_length=100, unique=True)
    slug_name = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)


class BlogCategoryManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(is_active=True).prefetch_related('postcategory_set')

    def per_category(self, filter_value):
        return self.prefetch_related(
            Prefetch(
                'postcategory_set',
                queryset=PostCategory.objects.prefetch_related(
                    Prefetch(
                        'post_set',
                        queryset=Post.objects.prefetch_related(
                            'has_tags'
                        )
                    )
                ))
        ).get(slug_name=filter_value)


class BlogCategory(TimeStampModel):

    name = models.CharField(max_length=100, verbose_name='Blog Categories')

    slug_name = models.SlugField(max_length=100, unique=True, blank=True)

    objects = BlogCategoryManager()

    class Meta:
        verbose_name = 'Main Blog Category'
        verbose_name_plural = 'Main Blog categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)


class SiteCategoryManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(is_active=True)


class SiteCategory(TimeStampModel):

    name = models.CharField(max_length=100, verbose_name='Website Categories')

    slug_name = models.SlugField(max_length=100, unique=True, blank=True)

    objects = SiteCategoryManager()

    class Meta:
        verbose_name = 'Website Navigation Category'
        verbose_name_plural = 'Website Navigation Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(SiteCategory, self).save(*args, **kwargs)


class Comment(TimeStampModel):
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment[10]


class PostCategory(TimeStampModel):
    belongs_to = models.ForeignKey(BlogCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug_name = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Posts categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(PostCategory, self).save(*args, **kwargs)


def image_upload_path(instance, file_name):
    return '{}/{}/{}'.format(instance.created_on, instance.created_by, file_name)


class PostQuerySet(models.QuerySet):
    def featured_post(self, flags):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_FEATURE_DAYS)
        end_range = now
        return self.filter(
            is_active=True,
            flags=flags,
        ).filter(
            created_on__gt=start_range,
            created_on__lte=end_range,
        )


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def featured_post(self, flags):
        return self.get_queryset().featured_post(flags)


class Post(TimeStampModel):
    has_tags = models.ManyToManyField(Tags)
    belongs_to = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    hard_title = models.CharField(max_length=1000)
    soft_title = models.CharField(max_length=1000)
    title_image = models.ImageField(upload_to=image_upload_path)
    post_body_first = models.TextField()
    post_body_second = models.TextField(blank=True, null=True)
    highlight_content = models.TextField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(Comment, blank=True)
    flags = models.PositiveIntegerField(blank=True, null=True)
    # flag:1-3 - featured  flag:5-10 - picks
    slug_name = models.SlugField(max_length=1000, unique=True, blank=True)

    objects = PostManager()

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
    belongs_to = models.ForeignKey(Post, on_delete=models.CASCADE,)
    inter_post_sequence = models.PositiveIntegerField(default=1)
    inter_post_heading = models.CharField(max_length=200)
    inter_post_content_one = models.TextField()
    inter_post_content_one_url = models.URLField(max_length=1000, null=True, blank=True)

    inter_post_content_two = models.TextField(blank=True, null=True)
    inter_post_content_two_url = models.URLField(max_length=1000, null=True, blank=True)
    inter_post_content_three = models.TextField(blank=True, null=True)
    inter_post_content_three_url = models.URLField(max_length=1000, null=True, blank=True)

    highlight_content = models.TextField(blank=True, null=True)
    post_image = models.ImageField(upload_to=subpostcontentimage, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Post Heading '
        verbose_name_plural = 'Blog Posts Headings'
        ordering = ['inter_post_sequence']

    def __str__(self):
        return self.inter_post_heading


class SubPostListElements(TimeStampModel):
    belongs_to = models.ForeignKey(SubPostContent, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=True, blank=True)
    title_url = models.URLField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Sub Post List Element'
        verbose_name_plural = 'Sub Post List Elements'

    def __str__(self):
        return self.title


class ListElements(TimeStampModel):
    belongs_to = models.ForeignKey(SubPostListElements, on_delete=models.CASCADE)
    element = models.CharField(max_length=1000)
    element_url = models.URLField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'List Element '
        verbose_name_plural = 'List Elements'

    def __str__(self):
        return self.element

