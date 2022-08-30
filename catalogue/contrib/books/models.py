import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from catalogue.models import TimestampedModel
from catalogue.contrib.tags import constants as tag_constants

UserModel = get_user_model()


class Author(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_("Name"), max_length=254)
    user = models.ForeignKey(
        UserModel, related_name="authors", on_delete=models.CASCADE
    )
    notes = models.CharField(_("Notes"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author:detail", kwargs={"pk": self.pk})


class Book(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(_("Title"), max_length=254)
    authors = models.ManyToManyField(Author, related_name="books", verbose_name=_("Authors"))
    tags = models.ManyToManyField(
        "tags.Tag", related_name="books", verbose_name=_("Tags"), limit_choices_to={'use': tag_constants.BOOKS}, blank=True
    )
    notes = models.CharField(_("Notes"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
