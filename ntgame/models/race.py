# django modules
from django.db import models

class Race(models.Model):

    name = models.CharField(max_length=100, default='Human')

    class Meta:
        verbose_name_plural = 'Races'