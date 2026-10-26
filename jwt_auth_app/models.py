from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
        ADMIN = "ADMIN", "Admin"

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return self.username