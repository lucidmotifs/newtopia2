from django.contrib import admin

from ntmeta.models import Aspect, Component, Entity, Quality, DefaultValue

# Register your models here.
admin.site.register(Quality)
admin.site.register(Component)
admin.site.register(DefaultValue)

class AspectInline(admin.StackedInline):
    model = Aspect.entities.through
    extra = 1
    verbose_name = "Aspect"
    verbose_name_plural = "Aspects"
    show_change_link = True
    can_delete = True


class QualityInline(admin.StackedInline):
    model = Quality
    extra = 1
    verbose_name = "Quality"
    verbose_name_plural = "Qualities"
    show_change_link = True
    can_delete = True


@admin.register(Aspect)
class AspectAdmin(admin.ModelAdmin):
    inlines = [
        QualityInline,
    ]
    exclude = ('entities', )


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_aspects')
    inlines = [
        AspectInline,
    ]

    def get_aspects(self, obj):
        return ", ".join([a.name for a in obj.aspect_set.all()])

    def get_components(self, obj):
        return ", ".join([c.name for c in obj.component_set.all()])
