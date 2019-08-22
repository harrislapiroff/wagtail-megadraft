from django.db import models
from wagtailmegadraft.widgets import MegadraftWidget


class MegadraftField(models.Field):

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {'widget': MegadraftWidget()}
        defaults.update(kwargs)
        return super().formfield(**defaults)
