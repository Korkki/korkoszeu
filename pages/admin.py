from django.contrib import admin
from .models import Page
from django.utils.translation import ugettext_lazy as _


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
