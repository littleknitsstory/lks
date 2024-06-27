from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class Hub(models.Model):
    """ """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="hub_user",
    )

    # tg_link
    # inst_link
    # phonenumber

    class Meta:
        verbose_name = _("Hub")
        verbose_name_plural = _("Hubs")
