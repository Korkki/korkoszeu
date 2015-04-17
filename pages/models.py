from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel


class PublishedPages(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Page(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=50)
    slug = models.SlugField(verbose_name=_("slug"), max_length=55, unique=True, db_index=True)
    description = models.CharField(verbose_name=_("description"), max_length=200, blank=True)
    content = models.TextField(verbose_name=_("content"))
    publish = models.BooleanField(verbose_name=_("published"), default=False)
    template_name = models.CharField(verbose_name=_("template name"), max_length=70, blank=True)
    sites = models.ManyToManyField(Site, verbose_name=_("sites"), related_name='pages')
    last_mod = models.DateTimeField(verbose_name=_("last modification"), auto_now=True)
    creation_date = models.DateTimeField(verbose_name=_("creation date"), auto_now_add=True)

    published = PublishedPages.as_manager()

    class Meta:
        verbose_name = _("page")
        verbose_name_plural = _("pages")
        get_latest_by = "creation_date"
        ordering = ['-creation_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', kwargs=dict(slug=self.slug))
