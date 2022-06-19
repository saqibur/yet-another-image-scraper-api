from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from apps.core.models import BaseModel


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    name = models.CharField(
        verbose_name="Name",
        db_column="name",
        max_length=255,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name="Email",
        db_column="email",
        blank=True,
        null=True,
        unique=True,
    )

    USERNAME_FIELD = "email"
    password = None

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
