from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Technology(MPTTModel):
    name = models.CharField(verbose_name=_("name"), max_length=50, db_index=True, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    icon = models.URLField(verbose_name=_("icon"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("technology")
        verbose_name_plural = _("technologies")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    @property
    def projects_count(self):
        return self.get_descendants(include_self=True).annotate(project_count=models.Count('projects'))\
            .aggregate(models.Sum('project_count')).get('project_count__sum', 0)


class Project(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255, db_index=True, unique=True)
    url = models.URLField(verbose_name=_("url"), max_length=255, blank=True)
    screenshot = models.URLField(verbose_name=_("screen"), max_length=255, blank=True)
    description = models.TextField(verbose_name=_("description"), blank=True)
    duration = models.DurationField(verbose_name=_("duration"), blank=True, null=True)
    technologies = models.ManyToManyField(Technology, verbose_name=_("technologies"), related_name='projects')

    def __str__(self):
        return self.name
