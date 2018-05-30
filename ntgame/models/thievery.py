# django modules
from django.db import models

class Thievery(models.Model):

    land = models.IntegerField(default=1000)

    class Meta:
        verbose_name_plural = 'Infrastructures'