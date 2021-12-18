import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from catalogue.models import TimestampedModel

UserModel = get_user_model()


class Tag(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_("Name"), max_length=254)
    author = models.ForeignKey(
        UserModel, related_name="tags", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags:detail", kwargs={"pk": self.pk})
