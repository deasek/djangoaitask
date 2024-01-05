import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Base Abstract model for AI test assignment
    """

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True
    )  # as it's a good practice to use UUID instead of sequentional pks
    created = models.DateTimeField(
        auto_now_add=True, null=True, editable=False, verbose_name=_("Created at")
    )
    modified = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name=_("Modified at")
    )

    class Meta:
        abstract = True
