import uuid
from django.db import models


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(null=False, unique=True)
    instructor = models.CharField(max_length=150, null=False)
    language = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    tagline = models.CharField(max_length=150, null=True)
    price = models.IntegerField(null=False)
    active = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, null=False)
    duration = models.IntegerField(null=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='courses')
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    resource = models.FileField(upload_to='media/resource')

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tag = models.CharField(max_length=150, null=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.tag
