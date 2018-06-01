from django.db import models

from .choices import QualityTypeChoices


class Entity(models.Model):
    CLASS_TEMPLATE = \
    """
    class {name}(models.Model):
        entity = models.ForeignKey(
            'ntmeta.Entity', on_delete=models.CASCADE, default={id})
        {attributes}
    """

    # django fields
    name = models.CharField(max_length=100, unique=True)

    def gen_game_model(self):
        # @TODO move to strings/templates module

        attr_fields = []
        for a in self.aspect_set.all():
            attr_fields.append(q.gen_attr_field() for q in a.quality_set.all())

        return Entity.CLASS_TEMPLATE % ({
            'name': self.name,
            'id': self.id,
            'attributes': '\n'.join(attr_fields),
        })

    class Meta:
        verbose_name_plural = 'Entities'

    def __str__(self):
        return self.name


class Aspect(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    entities = models.ManyToManyField(Entity, blank=True)

    def __str__(self):
        return self.name


class Quality(models.Model):
    FIELD_TEMPLATE = "%(label)s = %(field)s(%(args)s%(kwargs)s)"
    # should be loaded from QualityFieldArgs (args) when done
    max_length = 255

    label = models.CharField(max_length=50, unique=False)
    data_type = models.CharField(choices=QualityTypeChoices, max_length=20)
    description = models.CharField(max_length=255, default='No Description')
    nullable = models.BooleanField(default=False)
    blank = models.BooleanField(default=False)


    # relationships
    aspect = models.ForeignKey(
        Aspect, blank=True, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'Qualities'

    def __str__(self):
        return '{} {} ({})'.format(
            self.aspect, self.label.capitalize(), self.data_type)


class Component(models.Model):
    """ We could potentially use managers for System related components """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True, default=None)
    assigned = models.ManyToManyField(Entity)

    def __str__(self):
        return self.name


class DefaultValue(models.Model):
    """ Use a duo-key (Entity, Quality) to serve as a look-up for default
        values. """
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(
            self.entity.name, self.quality.label.capitalize(), self.value)
