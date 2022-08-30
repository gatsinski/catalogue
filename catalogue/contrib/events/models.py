import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from catalogue.models import TimestampedModel
from catalogue.contrib.tags import constants as tag_constants
from .constants import EVENT_TYPES, CONCERT

UserModel = get_user_model()


class Event(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_("Name"), max_length=254)
    type = models.CharField(_('Type'), max_length=254, choices=EVENT_TYPES, default=CONCERT)
    location = models.CharField(_("Location"), max_length=254)
    user = models.ForeignKey(
        UserModel, related_name="events", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        "tags.Tag", related_name="events", verbose_name=_("Tags"), limit_choices_to={'use': tag_constants.EVENTS}, blank=True
    )
    notes = models.CharField(_("Notes"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})
