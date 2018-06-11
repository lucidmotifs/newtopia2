# django modules
from django.db import models

from ntgame.models.province import Province
from ntgame.models.entities import (
    Soldier, OffensiveSpecialist, DefensiveSpecialist, Elite)


class Military(models.Model):

    province = models.OneToOneField(
        Province, null=False, on_delete=models.CASCADE, default=1)

    attack_time = models.FloatField("Base attack time", default=20)
    general_count = models.IntegerField(default=5)

    soldiers = models.OneToOneField(
        Soldier, on_delete=models.CASCADE, null=False, blank=False)
    offspec = models.OneToOneField(
        OffensiveSpecialist, on_delete=models.CASCADE, null=False, blank=False)
    defspec = models.OneToOneField(
        DefensiveSpecialist, on_delete=models.CASCADE, null=False, blank=False)
    elites = models.OneToOneField(
        Elite, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Militaries'
