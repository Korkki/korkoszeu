from django.views.generic import DetailView, TemplateView
from .models import Page


class IndexView(TemplateView):
    template_name = 'index.html'


class PageView(DetailView):
    model = Page
