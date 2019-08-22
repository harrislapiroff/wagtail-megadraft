=================
Wagtail Megadraft
=================

A very nice rich content editor.

Generate static files:
======================

.. code-block:: bash

   npm install    # install npm dependencies (must do first)
   npm run build  # build prod quality files once OR
   npm run start  # watch files for changes and rebuild devtool compatible files

Usage
=====

Add ``'wagtailmegadraft'`` to ``INSTALLED_APPS`` in your settings.

.. code-block:: python

   from wagtail.core.models import Page
   from wagtail.admin.edit_handlers import FieldPanel
   from wagtailmegadraft.fields import MegadraftField


   class MyPage(Page):
       content = MegadraftField(
           blank=True,
           null=True,
       )

       content_panels = Page.content_panels + [
           # Megadraft field doesn't need a special panel
           FieldPanel('content'),
       ]
