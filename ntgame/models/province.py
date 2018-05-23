from django.db import models

from ntgame.models.kingdom import Kingdom
from ntgame.models.military import Military

class Province(models.Model):
    # basic attributes
    name = models.CharField("Province Name", max_length=200, null=False)
    ruler = models.CharField("Ruler Name", max_length=60, null=False)

    # define relationships to other Game Models / Systems
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, default=1, null=False,
        blank=False)

    kingdom = models.ForeignKey(
        Kingdom, on_delete=models.CASCADE, null=False, blank=False, default=1)

    military = models.OneToOneField(
        Military, null=False, on_delete=models.CASCADE, default=1)
    
    infrastructure = models.OneToOneField(
        Infrastructure, null=False, on_delete=models.CASCADE, default=1)

    race = models.ForeignKey(
        Race, null=False, on_delete=models.CASCADE, default=1)

    science = models.OneToOneField(
        Science, null=False, on_delete=models.CASCADE, default=1)

    magic = models.OneToOneField(
        Magic, null=False, on_delete=models.CASCADE, default=1)

    thievery = models.OneToOneField(
        Thievery, null=False, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return "%s of %s (%d:%d)" % \
            ( self.name,
              self.kingdom.name,
              self.kingdom.island,
              self.kingdom.number )

### End Model Code. Entity Generation Below ###

class Peasant(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=1)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    growth_rate = models.FloatField(default='10.0')
    amount_total = models.IntegerField(default='1000')


class Bushel(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=3)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default='10000')


class GoldCoin(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=4)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default='50000')


class Rune(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=5)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)
    growth_rate = models.FloatField(default='-5.0')

