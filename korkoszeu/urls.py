from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from pages.views import PageView, IndexView
from portfolio.views import ProjectList

sitemaps = {}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^portfolio/$', ProjectList.as_view(), name='portfolio'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    url(_(r'^(?P<slug>[-\w]+)/$'), PageView.as_view(), name='page'),
    url(_(r'^$'), IndexView.as_view(), name='index'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))] + urlpatterns
