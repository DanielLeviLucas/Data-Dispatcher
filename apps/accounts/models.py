from uuid import uuid4
from secrets import token_urlsafe

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Account(models.Model):
    account_id = models.UUIDField(_("Unique account id"), default=uuid4, editable=False, unique=True)
    email_id = models.EmailField(_(" E-mail"), unique=True)
    app_secret_token = models.CharField(_("App secret token"), max_length=50, default=token_urlsafe, unique=True)
    account_name = models.CharField(_("Account name"), max_length=50, unique=True)
    website = models.URLField(_("Account website url"), null=True, blank=True)

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return f"{self.account_name} - {self.email_id}"

    def save(self, *args, **kwargs):
        if not self.account_name:
            raise ValidationError("Account name field cannot be empty.")
        if not self.email_id:
            raise ValidationError("Email field cannot be empty.")
        super(Account, self).save(*args, **kwargs)
