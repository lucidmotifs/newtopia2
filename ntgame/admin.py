from django.contrib import admin

from ntgame.models import Kingdom
from ntgame.models import Province, Peasant, Bushel, GoldCoin, Rune
from ntgame.models import (
    Military, Soldier, OffensiveSpecialist, DefensiveSpecialist, Elite)

### ProvinceAdmin Start ###

admin.site.register(Kingdom)

class PeasantInline(admin.StackedInline):
    model = Peasant
    readonly_fields = ('entity',)
    verbose_name = "Peasant"
    verbose_name_plural = "Peasants"
    show_change_link = True
    can_delete = False


class BushelInline(admin.StackedInline):
    model = Bushel
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Bushel"
    verbose_name_plural = "Bushels"
    show_change_link = True
    can_delete = False


class GoldCoinInline(admin.StackedInline):
    model = GoldCoin
    readonly_fields = ('entity',)
    verbose_name = "Gold Coin"
    verbose_name_plural = "Gold Coins"
    show_change_link = True
    can_delete = False


class RuneInline(admin.StackedInline):
    model = Rune
    readonly_fields = ('entity',)
    verbose_name = "Rune"
    verbose_name_plural = "Runes"
    show_change_link = True
    can_delete = False


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    ### entity inlines
    inlines = [
        PeasantInline,
        BushelInline,
        GoldCoinInline,
        RuneInline,
    ]

### ProvinceAdmin End ###

### MilitaryAdmin Start ###

class SoldierInline(admin.StackedInline):
    model = Soldier
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Soldier"
    verbose_name_plural = "Soldiers"
    show_change_link = True
    can_delete = False


class OffspecInline(admin.StackedInline):
    model = OffensiveSpecialist
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Offspec"
    verbose_name_plural = "OffSpec"
    show_change_link = True
    can_delete = False


class DefspecInline(admin.StackedInline):
    model = DefensiveSpecialist
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Defspec"
    verbose_name_plural = "Defspec"
    show_change_link = True
    can_delete = False


class EliteInline(admin.StackedInline):
    model = Elite
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Elite"
    verbose_name_plural = "Elite"
    show_change_link = True
    can_delete = False


@admin.register(Military)
class MilitaryAdmin(admin.ModelAdmin):
    ### entity inlines
    inlines = [
        SoldierInline,
        OffspecInline,
        DefspecInline,
        EliteInline,
    ]
