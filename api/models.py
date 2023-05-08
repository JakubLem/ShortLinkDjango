from django.db import models


class ProtocolChoices(models.TextChoices):
    HTTP = 'h', 'http'
    HTTPS = 's', 'https'


class BetterLink(models.Model):
    old_long_link_proto = models.CharField(
        max_length=1,
        choices=ProtocolChoices.choices,
        default=ProtocolChoices.HTTP,
    )
    old_link_url = models.CharField(max_length=255)
    short_link = models.CharField(max_length=64, unique=True)

    @property
    def old_link_view(self):
        return f"{self.get_old_long_link_proto_display()}://{self.old_link_url}"

    def __str__(self):
        return f"{self.old_link_view} -> {self.short_link}"

    @property
    def view(self):
        return {
            "old_link": f"{self.get_old_long_link_proto_display()}://{self.old_link_url}",
            "short_link": f"http://localhost:8000/api/blsr/{self.short_link}"
        }
