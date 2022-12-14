from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    STATUS_CHOICE= (
        ('p', 'published'),
        ('d', 'Draft')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    pulish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    
    
    def __str__(self):
        return self.title