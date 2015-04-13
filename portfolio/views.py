from django.views.generic import ListView
from portfolio.models import Project


class ProjectList(ListView):
    model = Project
