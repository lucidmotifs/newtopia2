from django.db import models

class Province(models.Model):
    # basic attributes
    name = models.CharField("Province Name", max_length=200, null=False)
    ruler = models.CharField("Ruler Name", max_length=60, null=False)

    # define relationships to other Game Models / Systems
    owner = models.ForeignKey('auth.User',
        on_delete=models.CASCADE,
        default=1,
        null=False,
        blank=False)

    # Kingdom

    # Infrastrcture

    # Military

### End Model Code. Entity Generation Below ###

class Peasant(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=1)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    growth_rate = models.FloatField(default=0.0)
    amount_total = models.IntegerField(default=0)


class Bushel(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=3)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)


class GoldCoin(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=4)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)


class Rune(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=5)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE, blank=True)
    amount_total = models.IntegerField(default=0)
    growth_rate = models.FloatField(default='-5.0')

