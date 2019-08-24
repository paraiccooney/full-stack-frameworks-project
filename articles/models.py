from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=50, default='')
    content = models.TextField()
    # auto_now_add=True will add the current data & time upon upload
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.headline