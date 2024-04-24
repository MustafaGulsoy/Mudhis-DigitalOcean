from django.db import models


# Create your models here.
class Child(models.Model):
    name = models.CharField(max_length=255)


class Member(models.Model):
    name = models.CharField(max_length=255)
    bird_date = models.DateField(auto_now_add=True)
    sex = models.BooleanField()

    date = models.DateField(auto_now_add=True)

    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(Child, related_name='likes')


