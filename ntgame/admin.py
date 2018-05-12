from django.contrib import admin

from ntgame.models import Province, Peasant, Bushel, GoldCoin, Rune

admin.site.register(Peasant)

class PeasantInline(admin.TabularInline):
    model = Peasant
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Peasant"
    verbose_name_plural = "Peasants"
    show_change_link = True
    can_delete = False


class BushelInline(admin.TabularInline):
    model = Bushel
    max_num = 1
    readonly_fields = ('entity',)
    verbose_name = "Bushel"
    verbose_name_plural = "Bushels"
    show_change_link = True
    can_delete = False


class GoldCoinInline(admin.TabularInline):
    model = GoldCoin
    extra = 1
    readonly_fields = ('entity',)
    verbose_name = "GoldCoin"
    verbose_name_plural = "GoldCoins"
    show_change_link = True
    can_delete = False


class RuneInline(admin.TabularInline):
    model = Rune
    extra = 1
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