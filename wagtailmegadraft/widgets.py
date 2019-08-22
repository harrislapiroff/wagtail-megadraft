import json

from django.forms import Media, widgets
from wagtail.utils.widgets import WidgetWithScript


class MegadraftWidget(WidgetWithScript, widgets.HiddenInput):
    options = {}

    def render_js_init(self, id_, name, value):
        return (
            "window.wagtailmegadraft.initEditor("
            "'#{id}', {opts}, document.currentScript"
            ")"
        ).format(
            id=id_,
            opts=json.dumps(self.options)
        )

    class Media:
        js = ('wagtailmegadraft/wagtailmegadraft.js',)
        css = {
            'all': ('wagtailmegadraft/wagtailmegadraft.css',)
        }
