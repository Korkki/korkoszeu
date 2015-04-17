from modeltranslation.translator import translator, TranslationOptions
from .models import Page


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content', 'slug')

translator.register(Page, PageTranslationOptions)
