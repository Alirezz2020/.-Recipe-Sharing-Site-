import uuid
from django.db import models
from django.contrib.auth.models import User


def profile_picture_upload_path(instance, filename):
    return f'profile_pictures/{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to=profile_picture_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # If the user hasn’t provided a unique ID, generate one.
            self.unique_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'
