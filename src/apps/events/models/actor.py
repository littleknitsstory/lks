from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class Actor(models.Model):
    """ """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("User"),
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
