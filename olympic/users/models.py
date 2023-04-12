import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country_choice = (
        ("JPN", "Japan"),
        ("USA", "USA"),
        ("UK", "England"),
        ("NP", "Nepal")
    )

    # customizing fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)
    country = models.CharField(max_length=25, choices=country_choice)

   
    # here, email is already a required field
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username