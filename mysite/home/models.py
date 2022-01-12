from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    # Поля в базе данных
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Подзаголовок')

    # Поля для ввода данных в интерфейсе администратора.

    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]