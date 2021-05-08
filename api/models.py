from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserInfo(AbstractUser):
    token = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='articles')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']
        verbose_name = '博客'
        verbose_name_plural = verbose_name


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']