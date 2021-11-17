from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Title
    title = models.CharField(max_length=128)
    # text
    text = models.TextField(blank=True)
    # author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_date
    created_date = models.DateTimeField(auto_now_add=True)
    # modified_date
    modified_date = models.DateTimeField(auto_now=True)
    # published_date
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    # name
    name = models.CharField(max_length=128, unique=True)
    # description
    description = models.TextField(blank=True)
    # posts
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name