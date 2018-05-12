# django modules
from django.db import models

from ntgame.models.province import Province

class Military(models.Model):

    province = models.OneToOneField(Province,
        null = True,
        on_delete=models.CASCADE,
        primary_key=False)

### End Model Code. Entity Generation Below ###

class Soldier(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=6)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)
    offensive_strength_value = models.IntegerField(default=0)
    defensive_strength_value = models.IntegerField(default=0)
    consumes = models.ForeignKey('GoldCoin', on_delete=models.CASCADE)


class OffensiveSpecialist(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=7)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    offensive_strength_value = models.IntegerField(default=0)
    amount_total = models.IntegerField(default=0)


class DefensiveSpecialist(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=8)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    defensive_strength_value = models.IntegerField(default=0)
    amount_total = models.IntegerField(default=0)


class Elite(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=9)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    offensive_strength_value = models.IntegerField(default=0)
    defensive_strength_value = models.IntegerField(default=0)
    amount_total = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    cost_currency = models.ForeignKey('GoldCoin', on_delete=models.CASCADE)
    cost_scaling = models.FloatField(default=0.0)

