from django.contrib.auth.models import AbstractUser,Permission
from django.contrib.auth.models import Group as AuthGroup  # Rename the Group model to avoid conflicts
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Add any additional fields you need here

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        AuthGroup,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',  # You can change this to your preferred name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',  # You can change this to your preferred name
    )
