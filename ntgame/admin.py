from django.contrib import admin

from ntgame.models import Kingdom
from ntgame.models import Province
from ntgame.models import Military
from ntgame.models import Infrastructure
from ntgame.models import Science
from ntgame.models import Magic
from ntgame.models import Thievery
from ntgame.models.entities import (
    Food, Peasant, GoldCoin, Rune, Soldier, OffensiveSpecialist, 
    DefensiveSpecialist, Elite, Mage, Thief)

# Province Start
admin.site.register(Kingdom)
admin.site.register(Food)
admin.site.register(Peasant)
admin.site.register(GoldCoin)
admin.site.register(Rune)

# Military Start
admin.site.register(OffensiveSpecialist)
admin.site.register(DefensiveSpecialist)
admin.site.register(Elite)
admin.site.register(Soldier)

# Magic
admin.site.register(Mage)

# Thievery
admin.site.register(Thief)


class MilitaryInline(admin.StackedInline):
    model = Military
    max_num = 1
    verbose_name = "Military"
    verbose_name_plural = "Military"
    show_change_link = True
    can_delete = False


class InfrastructureInline(admin.TabularInline):
    model = Infrastructure
    max_num = 1
    extra = 1
    verbose_name = "Infrastructure"
    verbose_name_plural = "Infrastructure"
    show_change_link = True
    can_delete = False


class MagicInline(admin.TabularInline):
    model = Magic
    max_num = 1
    verbose_name = "Magic"
    verbose_name_plural = "Magic"
    show_change_link = True
    can_delete = False


class ThieveryInline(admin.TabularInline):
    model = Thievery
    max_num = 1
    verbose_name = "Thievery"
    verbose_name_plural = "Thievery"
    show_change_link = True
    can_delete = False


class ScienceInline(admin.TabularInline):
    model = Science
    max_num = 1
    verbose_name = "Science"
    verbose_name_plural = "Science"
    show_change_link = True
    can_delete = False


class InfrastructureAdmin(admin.ModelAdmin):
    pass


class ScienceAdmin(admin.ModelAdmin):
    pass


class MagicAdmin(admin.ModelAdmin):
    pass


class ThieveryAdmin(admin.ModelAdmin):
    pass


class MilitaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
        ('Entities', {
            'classes': ('collapse',),
            'fields': ('soldiers', 'offspec', 'defspec', 'elites'),
        }),
    )


class ProvinceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'ruler', 'owner', 'kingdom')
        }),
        ('Entities', {
            'classes': ('collapse',),
            'fields': ('peasants', 'food', 'runes', 'gold_coins'),
        }),
    )

    inlines = [
        MilitaryInline, InfrastructureInline, ScienceInline,
        MagicInline, ThieveryInline]


admin.site.register(Province, ProvinceAdmin)
admin.site.register(Military, MilitaryAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(Magic, MagicAdmin)
admin.site.register(Thievery, ThieveryAdmin)
