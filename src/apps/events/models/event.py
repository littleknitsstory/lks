import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from optimized_image.fields import OptimizedImageField


logger = logging.getLogger(__name__)
User = get_user_model()


class ImagesMixin(models.Model):
    """
    Abstract model for basic images information
    Attributes:
    image_preview: path images
    image_alt (char): image_alt for <img>
    """

    image_preview = OptimizedImageField(_("Images"), blank=True)
    image_alt = models.CharField(_("Images Alt"), blank=True, max_length=255)

    class Meta:
        abstract = True

    def get_image(self) -> str:
        try:
            image = self.image_preview.url
        except ValueError:
            image = None
        return image


class EventTag(models.Model):
    """Tag model"""

    title = models.CharField(_("Title"), max_length=64)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class EventLocation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Event(ImagesMixin):
    title = models.CharField(_("Title"), max_length=120)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    is_active = models.BooleanField(_("Active"), default=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    start_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    end_at = models.DateTimeField(_("Updated at"), auto_now=True)
    location = models.ForeignKey(
        EventLocation,
        related_name="event_location",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        EventTag, related_name="event_tags", blank=True
    )
    # website_link
    # tg_link
    # inst_link
    # phonenumber
    # created_by

    event_type = models.CharField(
        _("Type Event"), max_length=120, null=True, blank=True
    )


    #?
    meta_title = models.CharField(_("Title Seo"), max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(_("Keywords"), blank=True, null=True)
    meta_description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    categories = models.ManyToManyField(
        "EventCategory",
        verbose_name=_("Category"),
        related_name="product_categories",
        blank=True,
    )
    author = models.ForeignKey(
        User,
        related_name="event_author",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.title}"




class EventPhoto(ImagesMixin):
    event = models.ForeignKey(
        "Event",
        verbose_name=_("Event"),
        on_delete=models.CASCADE,
        related_name="photo_event",
    )

    class Meta:
        verbose_name = _("Event photo")
        verbose_name_plural = _("Event photos")

    def __str__(self):
        return f"{self.product}"


class EventSimilar(models.Model):
    event = models.ForeignKey(
        "Event",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="similar_product",
    )
    events = models.ManyToManyField(
        "Events", verbose_name=_("Events"), related_name="similar_events",
    )

    class Meta:
        verbose_name = (_("Event Similar"),)
        verbose_name_plural = _("Events Similar")

    def __str__(self):
        return f"{self.event}"
