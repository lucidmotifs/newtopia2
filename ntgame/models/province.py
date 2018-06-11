from django.db import models

from ntgame.models.entities import (Peasant, Rune, GoldCoin, Food)
from ntgame.models.kingdom import Kingdom
from ntgame.models.race import Race


class Province(models.Model):
    # basic attributes
    name = models.CharField("Province Name", max_length=200, null=False)
    ruler = models.CharField("Ruler Name", max_length=60, null=False)

    # entities
    peasants = models.OneToOneField(
        Peasant, on_delete=models.CASCADE, null=False, blank=False)
    runes = models.OneToOneField(
        Rune, on_delete=models.CASCADE, null=False, blank=False)
    gold_coins = models.OneToOneField(
        GoldCoin, on_delete=models.CASCADE, null=False, blank=False)
    food = models.OneToOneField(
        Food, on_delete=models.CASCADE, null=False, blank=False)

    # define relationships to other Game Models / Systems
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, default=1, null=False,
        blank=False)

    kingdom = models.ForeignKey(
        Kingdom, on_delete=models.CASCADE, null=False, blank=False, default=1)

    race = models.ForeignKey(
        Race, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s of %s" % \
            ( self.name,
              str(self.kingdom))
