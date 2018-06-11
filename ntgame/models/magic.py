# django modules
from django.db import models
from ntgame.models.province import Province
from ntgame.models.entities import Mage


class Magic(models.Model):

    province = models.OneToOneField(
        Province, null=False, on_delete=models.CASCADE, default=1)

    mana = models.IntegerField(default=100)

    mages = models.OneToOneField(
        Mage, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Magic Models'