# django modules
from django.db import models
from ntgame.models.province import Province


class Infrastructure(models.Model):

    province = models.OneToOneField(
        Province, null=False, on_delete=models.CASCADE, default=1)

    land = models.IntegerField(default=1000)

    class Meta:
        verbose_name_plural = 'Infrastructures'