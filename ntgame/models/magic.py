# django modules
from django.db import models

class Magic(models.Model):

    mana = models.IntegerField(default=100)

    class Meta:
        verbose_name_plural = 'Magic Models'