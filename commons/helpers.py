from wagtail.blocks import StructValue
from wagtail.images.blocks import ImageChooserBlock


class ImageChooserForOldSVG(ImageChooserBlock):
    """Workaround to fix and replace old SVG Fields with standar ImageChooser"""

    def bulk_to_python(self, values):
        new_values = []
        posible_component_names = [
            "image",
            "icon",
            "avatar",
            "background_image",
            "background_illustration",
        ]

        for value in values:
            if isinstance(value, (dict, StructValue)):
                for posible_component_name in posible_component_names:
                    if posible_component_name in value:
                        new_values.append(value[posible_component_name])
        new_bulk = super().bulk_to_python(new_values)
        return new_bulk
