from django.test import TestCase
import factory
from factory import django as dj_factory
from portfolio import models
from faker import Factory
fake = Factory.create('pl_PL')


class TechnologyFactory(dj_factory.DjangoModelFactory):
    class Meta:
        model = models.Technology
        django_get_or_create = ('name',)

    name = factory.sequence(lambda n: 'name %d' % n)


class ProjectFactory(dj_factory.DjangoModelFactory):
    class Meta:
        model = models.Project
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'name %d' % n)
    url = factory.Sequence(lambda n: fake.url())
    screenshot = factory.Sequence(lambda n: fake.url())
    description = factory.Sequence(lambda n: fake.text())

    @factory.post_generation
    def technologies(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tech in extracted:
                self.technologies.add(tech)


class TechnologyTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TechnologyTest, cls).setUpClass()
        tech1 = TechnologyFactory(name='Python')
        tech2 = TechnologyFactory(name='Django', parent=tech1)
        ProjectFactory(technologies=(tech2,))
        ProjectFactory(technologies=(tech1,))

    def test_project_count(self):
        tech1 = models.Technology.objects.filter(name='Python').first()
        self.assertEqual(tech1.projects_count, 2)

        tech2 = models.Technology.objects.filter(name='Django').first()
        self.assertEqual(tech2.projects_count, 1)
