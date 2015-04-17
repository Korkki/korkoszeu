from django.test import TestCase
from django.utils.text import slugify
import factory
from factory import django as dj_factory
from pages import models
from faker import Factory
fake = Factory.create('pl_PL')


class PageFactory(dj_factory.DjangoModelFactory):
    class Meta:
        model = models.Page
        django_get_or_create = ('title', 'slug', 'content')

    title = factory.Sequence(lambda n: 'title %d' % n)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    content = factory.Sequence(lambda n: fake.text())
