from modeltranslation.translator import translator, TranslationOptions
from .models import Technology, Project


class TechnologyTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Project, ProjectTranslationOptions)
translator.register(Technology, TechnologyTranslationOptions)
