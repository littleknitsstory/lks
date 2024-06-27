import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)
User = get_user_model()


class EventTicket(models.Model):
    name = models.CharField(
        "Название", help_text="example: Month Standard", blank=False
    )

    event = models.ForeignKey(
        "Event",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="event_ticket",
    )

    sale = models.DecimalField(
        _("Sale"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0,
    )

    price = models.DecimalField(
        max_digits=6, decimal_places=2
    )

    currency = models.CharField(_("Currency"), default="EUR", max_length=3)
    count = models.IntegerField(verbose_name=_("Count"), blank=True, default=1)

    class Meta:
        verbose_name = _("Event Ticket")
        verbose_name_plural = _("Event Tickets")
        ordering = ("-created_at",)
