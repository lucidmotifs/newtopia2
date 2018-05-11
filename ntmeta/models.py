from django.db import models

from .choices import QualityTypeChoices

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Entities'

    def __str__(self):
        return self.name


class Aspect(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    entities = models.ManyToManyField(Entity, blank=True)

    def __str__(self):
        return self.name


class Quality(models.Model):
    label = models.CharField(max_length=50, unique=False)
    data_type = models.CharField(choices=QualityTypeChoices, max_length=20)
    aspect = models.ForeignKey(Aspect, blank=True, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'Qualities'

    def __str__(self):
        return self.label    


class Component(models.Model):
    """ We could potentially use managers for System related components """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True, default=None)
    assigned = models.ManyToManyField(Entity)

    def __str__(self):
        return self.name
