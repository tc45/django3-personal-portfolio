from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(null=True)
    body = models.TextField(max_length=30000)
    image = models.ImageField(upload_to='blog/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title