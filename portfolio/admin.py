from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin
from portfolio.models import Project, Technology


class TechnologyAdmin(MPTTModelAdmin):
    list_display = ('name', 'projects_count')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_url')
    search_fields = ('name', 'url')
    list_filter = ('technologies',)

    def project_url(self, obj):
        return mark_safe('<a href="{0}" target="_blank">{0}</a>'.format(obj.url))
    project_url.allow_tags = True
    project_url.short_description = _('url')

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
