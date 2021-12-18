import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from catalogue.models import TimestampedModel

UserModel = get_user_model()


class Store(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_("Name"), max_length=254)
    user = models.ForeignKey(
        UserModel, related_name="stores", on_delete=models.CASCADE
    )
    notes = models.CharField(_("Notes"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stores:detail", kwargs={"pk": self.pk})
