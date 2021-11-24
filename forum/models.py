from django.db import models
from django.utils.text import slugify
from authentication.models import Account
from tinymce.models import HTMLField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = models.TextField(blank=True)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @property
    def last_reply(self):
        return Comment.objects.filter(post=self).latest('date')

    @property
    def num_comments(self):
        return Comment.objects.filter(post=self).count()

    @property
    def get_tags(self):
        return self.tags.split(',')


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def replies(self):
        return Reply.objects.filter(comment=self).all()


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "replies"