"""Posts models."""

# Django imports
from distutils.command.upload import upload
from django.db import models

# Models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""
    # foreign key
    user= models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    profile= models.ForeignKey('users.Profile', verbose_name=(""), on_delete=models.CASCADE)
    

    # data
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    # metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # methods

    def __str__(self):
        return f'{self.title} by @{self.user.username}'
    