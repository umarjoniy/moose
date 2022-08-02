from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=75)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class About(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author')
    subtitle = models.TextField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    social_media = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    def __str__(self):
        return self.name
# 17,42