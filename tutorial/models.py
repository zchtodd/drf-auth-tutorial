from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=255, unique=True, null=True)
    github_id = models.CharField(max_length=255, unique=True, null=True)

    def clean(self):
        if self.google_id is None and self.github_id is None:
            raise ValidationError("One of google_id or github_id must be set.")
