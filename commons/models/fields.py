from dataclasses import dataclass

from django.core.exceptions import ValidationError
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _

from commons.widgets import MultiURLWidget
from commons.validators import URLDomainValidator


@dataclass
class SocialNetwork:
    """Class to define SocialNetworks."""

    key: str
    label: str
    domain: str
    validator: object

    def __init__(self, key, label, domain):
        """Set values and create validator."""
        self.key = key
        self.label = label
        self.domain = domain
        self.validator = URLDomainValidator(domain)


class SocialNetworksField(JSONField):
    """Save social network urls as a Json object."""

    SOCIAL_NETWORKS = [
        SocialNetwork("facebook", "Facebook", "facebook.com"),
        SocialNetwork("instagram", "Instagram", "instagram.com"),
        SocialNetwork("tiktok", "Tiktok", "tiktok.com"),
        SocialNetwork("youtube", "Youtube", "youtube.com"),
        SocialNetwork("twitter", "Twitter", "twitter.com"),
    ]

    def formfield(self, **kwargs):
        """Override widget with `MultiURLWidget`."""
        return super().formfield(
            **{"widget": MultiURLWidget(self.SOCIAL_NETWORKS), **kwargs}
        )

    def validate(self, value, model_instance):
        """Extend validation to check that correct domain is used in each URL."""
        super().validate(value, model_instance)

        errors = []
        has_urls = False
        for index, url in value.items():
            if not url:
                continue
            has_urls = True
            network = next((x for x in self.SOCIAL_NETWORKS if x.key == index), None)
            try:
                network.validator(url)
            except ValidationError:
                errors.append(
                    ValidationError(
                        _(
                            "La URL para %(network)s no es válida. Ingrese una URL que"
                            " inicie con https://%(domain)s/ (ingresó %(url)s)."
                        ),
                        params={
                            "network": network.label,
                            "domain": network.domain,
                            "url": url,
                        },
                    )
                )

        if errors:
            raise ValidationError(errors)

        if not has_urls and not self.blank:
            raise ValidationError(_("Al menos una url es requerida."))