from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    STUDENT = 'student'
    PROFESSOR = 'professor'
    ADMIN = 'admin'

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return self.username
