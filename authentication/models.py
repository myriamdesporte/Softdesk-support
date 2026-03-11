from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    """
    Custom user model with GDPR compliance fields.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @property
    def age(self):
        """Calculate user's age from date of birth."""
        if self.date_of_birth is None:
            return None

        today = date.today()
        birth_date = self.date_of_birth
        return today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
        )
