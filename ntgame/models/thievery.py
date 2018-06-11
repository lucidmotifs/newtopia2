# django modules
from django.db import models
from ntgame.models.province import Province
from ntgame.models.entities import Thief


class Thievery(models.Model):

    province = models.OneToOneField(
        Province, null=False, on_delete=models.CASCADE, default=1)

    stealth = models.IntegerField(default=100)

    thieves = models.OneToOneField(
        Thief, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Thievery Models'