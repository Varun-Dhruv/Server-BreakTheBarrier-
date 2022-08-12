from django.db import models
from venv import create
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
GENDER_CHOICES = [
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
]


class BaseModel(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4()),
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# class User(BaseModel):
#     REQUIRED_FIELDS = ('user')
#     username=models.CharField(max_length=100 ,editable=False,primary_key=True),
#     password=models.CharField(max_length=100,)
#     gender=models.CharField(max_length=100,choices=GENDER_CHOICES)


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)

# Create your models here.
