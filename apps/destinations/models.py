
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.accounts.models import Account


class Destination(models.Model):
    class HttpMethod(models.TextChoices):
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        PATCH = "PATCH"
        DELETE = "DELETE"

    url = models.URLField(_("destination url"), null=True, blank=True)
    http_method = models.CharField(
        _("http method"), max_length=6, choices=HttpMethod.choices, default=HttpMethod.POST
    )
    account = models.ForeignKey(Account, related_name="destinations", on_delete=models.CASCADE)
    headers = models.JSONField(default=dict)

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")

    def __str__(self):
        return f"{self.url} - {self.http_method}"

    def save(self, *args, **kwargs):
        if not self.url:
            raise ValidationError("URL field cannot be empty.")
        super(Destination, self).save(*args, **kwargs)
