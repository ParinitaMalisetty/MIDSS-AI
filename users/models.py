from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        CITIZEN = "CITIZEN", "Citizen"
        ENGINEER = "ENGINEER", "Engineer"
        ADMIN = "ADMIN", "Admin"

    full_name = models.CharField(max_length=100)

    mobile_number = models.CharField(
        max_length=15,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CITIZEN
    )

    REQUIRED_FIELDS = [
        "mobile_number",
        "full_name",
    ]

    def __str__(self):
        return self.full_name