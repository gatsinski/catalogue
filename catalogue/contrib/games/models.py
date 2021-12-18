import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from catalogue.models import TimestampedModel

UserModel = get_user_model()


class Game(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(_("Title"), max_length=254)
    owner = models.ForeignKey(
        UserModel, related_name="games", on_delete=models.CASCADE
    )
    store = models.ForeignKey(
        "stores.Store",
        related_name="games",
        on_delete=models.CASCADE,
        verbose_name=_("Store"),
    )
    tags = models.ManyToManyField(
        "tags.Tag", related_name="games", verbose_name=_("Tags"), blank=True
    )
    notes = models.CharField(_("Notes"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("games:detail", kwargs={"pk": self.pk})
