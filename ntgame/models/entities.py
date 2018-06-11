from django.db import models


# --- generated entities below ---
class Peasant(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=1)
    amount = models.IntegerField('Total Number', blank=False, default='1500', null=False)


class Food(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=2)
    amount = models.IntegerField('Total Number', blank=False, default='10', null=False)


class GoldCoin(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=3)
    amount = models.IntegerField('Total Number', blank=False, default='50000', null=False)


class Rune(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=4)
    amount = models.IntegerField('Total Number', blank=False, default='0', null=False)
    growth_rate = models.FloatField('How fast an Entity grows per turn', blank=True, default='-5.0', null=True)


class Soldier(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=5)
    amount = models.IntegerField('Total Number', blank=False, default='500', null=False)
    offensive_strength_value = models.IntegerField('Offensive Power', blank=False, default='1', null=False)
    defensive_stength_value = models.IntegerField('Defensive Power', blank=False, default='1', null=False)


class DefensiveSpecialist(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=6)
    amount = models.IntegerField('Total Number', blank=False, default='0', null=False)
    defensive_stength_value = models.IntegerField('Defensive Power', blank=False, default='4', null=False)


class OffensiveSpecialist(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=7)
    amount = models.IntegerField('Total Number', blank=False, default='0', null=False)
    offensive_strength_value = models.IntegerField('Offensive Power', blank=False, default='4', null=False)


class Elite(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=8)
    amount = models.IntegerField('Total Number', blank=False, default='0', null=False)
    offensive_strength_value = models.IntegerField('Offensive Power', blank=False, default='4', null=False)
    defensive_stength_value = models.IntegerField('Defensive Power', blank=False, default='4', null=False)


class Thief(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=9)
    amount = models.IntegerField('Total Number', blank=False, default=0, null=False)


class Mage(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=10)
    amount = models.IntegerField('Total Number', blank=False, default=0, null=False)
    effectiveness_value = models.FloatField('Entity\'s power multiplier', blank=False, default=None, null=True)
