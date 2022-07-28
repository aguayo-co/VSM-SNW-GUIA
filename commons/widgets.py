"""Custom Form Widgets."""
import json

from django import forms


class MultiURLWidget(forms.MultiWidget):
    """Widget to capture multiple URLs compatible with JSON fields."""

    template_name = "commons/forms/widgets/multi_url_widget.html"

    def __init__(self, urls, attrs=None):
        """
        Create a widget for each provided URL combo.

        `urls` is an iterable of objects with the following keys:
         - key
         - label
        """
        self.urls = urls
        widgets = [forms.URLInput()] * len(urls)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        """Extract urls from Json."""
        values = []
        value = json.loads(value)
        if isinstance(value, dict):
            for url in self.urls:
                values.append(value.get(url.key))
        return values

    def value_from_datadict(self, data, files, name):
        """Return JSON encoded dict of Urls."""
        urls = super().value_from_datadict(data, files, name)
        data = json.dumps({url.key: urls[index] for index, url in enumerate(self.urls)})
        return data

    def get_context(self, name, value, attrs):
        """Add labels to each widget."""
        context = super().get_context(name, value, attrs)
        for index, url in enumerate(self.urls):
            context["widget"]["subwidgets"][index]["label"] = url.label
        return context
