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
    entity = models.OneToOneField('ntmeta.Entity', on_delete=models.CASCADE)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE)
    growth_rate = models.FloatField(default=0.0)
    amount_total = models.IntegerField(default=0)
    name_short = models.CharField(max_length=200, null=True, blank=True)
    name_abbr = models.CharField(max_length=200, null=True, blank=True)
    name_plural = models.CharField(max_length=200, null=True, blank=True)


class Bushel(models.Model):
    entity = models.OneToOneField('ntmeta.Entity', on_delete=models.CASCADE)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE)
    amount_total = models.IntegerField(default=0)
    name_short = models.CharField(max_length=200, null=True, blank=True)
    name_abbr = models.CharField(max_length=200, null=True, blank=True)
    name_plural = models.CharField(max_length=200, null=True, blank=True)


class GoldCoin(models.Model):
    entity = models.OneToOneField('ntmeta.Entity', on_delete=models.CASCADE)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE)
    amount_total = models.IntegerField(default=0)
    name_short = models.CharField(max_length=200, null=True, blank=True)
    name_abbr = models.CharField(max_length=200, null=True, blank=True)
    name_plural = models.CharField(max_length=200, null=True, blank=True)


class Rune(models.Model):
    entity = models.OneToOneField('ntmeta.Entity', on_delete=models.CASCADE)
    province = models.OneToOneField(
        'Province', on_delete=models.CASCADE)
    amount_total = models.IntegerField(default=0)
    name_short = models.CharField(max_length=200, null=True, blank=True)
    name_abbr = models.CharField(max_length=200, null=True, blank=True)
    name_plural = models.CharField(max_length=200, null=True, blank=True)
    growth_rate = models.FloatField(default=0.0)

