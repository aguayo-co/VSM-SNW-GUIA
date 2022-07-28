"""Custom Validators."""
import re

from django.core.validators import URLValidator


class URLDomainValidator(URLValidator):
    """
    Validate that the url is for a specific domain, with or without www.

    It enforces the use of secure (https) urls.
    """

    def __init__(self, domain, **kwargs):
        """Set Regex for the given domain."""
        # domain = domain.replace(".", "\.")
        regex = re.compile(r"^https://(?:www|co)?.?" + f"{domain}/")
        super().__init__(regex=regex, schemes=["https"], **kwargs)
