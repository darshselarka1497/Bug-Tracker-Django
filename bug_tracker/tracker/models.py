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

class Comment(models.Model):
    bug = models.ForeignKey(Bug, related_name='comments', on_delete = models.CASCADE)
    team_member = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']