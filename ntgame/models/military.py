# django modules
from django.db import models

class Military(models.Model):

    attack_time = models.FloatField("Base attack time", default=20)
    general_count = models.IntegerField(default=5)

    class Meta:
        verbose_name_plural = 'Militaries'

### End Model Code. Entity Generation Below ###

class Soldier(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=6)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)
    offensive_strength_value = models.IntegerField(default='1')
    defensive_strength_value = models.IntegerField(default='1')
    consumes = models.ForeignKey('ntmeta.Entity', on_delete=models.CASCADE, related_name='consumes')


class OffensiveSpecialist(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=7)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    offensive_strength_value = models.IntegerField(default='4')
    amount_total = models.IntegerField(default=0)


class DefensiveSpecialist(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=8)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    defensive_strength_value = models.IntegerField(default='4')
    amount_total = models.IntegerField(default=0)


class Elite(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=9)
    military = models.OneToOneField(
        'Military', on_delete=models.CASCADE, blank=True)
    offensive_strength_value = models.IntegerField(default=0)
    defensive_strength_value = models.IntegerField(default=0)
    amount_total = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    cost_currency = models.ForeignKey('ntmeta.Entity', on_delete=models.CASCADE, default='3', related_name='cost_currency')
    cost_scaling = models.FloatField(default=0.0)

