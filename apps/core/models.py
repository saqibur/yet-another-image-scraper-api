from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(
        verbose_name="UUID",
        db_column="uuid",
        unique=True,
        default=uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(
        verbose_name="Created at",
        db_column="created_at",
        auto_now_add=True,
        editable=False,
    )

    modified_at = models.DateTimeField(
        verbose_name="Modified at",
        db_column="modified_at",
        auto_now=True,
    )

    class Meta:
        abstract = True
