"""Workaround to prevent node_modules to be collected, but preserving sass autoprefixing."""
from django.conf import settings
from django.template import Library
from sass_processor.processor import SassProcessor
from sass_processor.templatetags.sass_tags import SassSrcNode

register = Library()


class SNWSassProcessor(SassProcessor):
    def __init__(self, path=None):
        super().__init__(path=path)
        self.node_modules_dir = settings.NODE_MODULES_PATH


class SNWSassSrcNode(SassSrcNode):
    def __init__(self, path):
        self.sass_processor = SNWSassProcessor(path)


@register.tag(name="sass_src")
def render_sass_src(parser, token):
    return SNWSassSrcNode.handle_token(parser, token)
