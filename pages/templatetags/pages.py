from django.template import Library
from pages.models import Page

register = Library()


@register.inclusion_tag('_main_menu.html')
def main_menu():
    return dict(pages=Page.published.all())