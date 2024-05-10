from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum


class Role(Enum):
    ADMIN = 1
    GUEST = 2
    PARENT = 3
    CHILD = 4


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=10, choices=[('male', 'Erkek'), ('female', 'Kadın')])
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
    pressure_data = models.TextField()  # Basınç verisi için
    motion_data = models.TextField()  # Hareket verisi için
    status = models.CharField(max_length=10, choices=['child', 'adult'])

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    role = Role.GUEST
    childs = models.ForeignKey("Child", on_delete=models.CASCADE)
