from django.db import models

# Create your models here.

class Bug(models.Model):
    title = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']   