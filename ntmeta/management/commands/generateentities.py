import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ntmeta.choices import QualityType
from ntmeta.models import DefaultValue
from ntmeta.models import Entity
from ntmeta.models import Quality
from ntmeta.systems.province import ProvinceSystem
from ntmeta.systems.military import MilitarySystem


class Command(BaseCommand):
    help = 'Creates entity models in specified app'

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='+', type=str)

    def handle(self, *args, **options):

        def gen_game_model(entity, attributes):
            return Entity.CLASS_TEMPLATE % ({
                'name': entity.name,
                'id': entity.id,
                'attributes': '\n'.join(attributes),
            })

        def gen_attr_fields(entity, aspect):
            attributes = []
            for q in aspect.quality_set.all():
                label = aspect.name.lower() if (
                    aspect.name.lower() == q.label) else '%s_%s' % (
                        aspect.name.lower().replace(' ', '_'), q.label)
                field = 'models.{}'.format(q.data_type)
                args = []
                if q.data_type == QualityType.ENTITY:
                    args.append('\'models.{}\''.format(q.entity))
                else:
                    args.append(q.description)
                
                kwargs = {}
                if q.data_type == 'CharField':
                    kwargs.update({
                        'max_length': q.max_length
                    })
                kwargs.update({
                    'null': q.nullable,
                    'blank': q.blank,
                })

                # check for a default value
                try:
                    default = DefaultValue.objects.get(
                        entity=entity, quality=q)
                    kwargs['default'] = '\'{}\''.format(default.default)
                except DefaultValue.DoesNotExist:
                    pass

                attr = Quality.FIELD_TEMPLATE.format(
                    label, field, ', '.join(args), ', '.join(
                        ['%s=%s' % (k, v) for k, v in kwargs.items()])
                )
                attributes.append(attr)

            return attributes

        # TODO fix, only want one app
        app = options['app'][0]
        assert app in settings.INSTALLED_APPS, '{} not found'.format(app)

        # move to models directory of `app`
        os.chdir(app+'/models')

        models = []
        for e in Entity.objects.all():
            attributes = [gen_attr_fields(e, a) for a in e.aspect_set.all()]
            models.append(gen_game_model(e, attributes))

        print('\n\n'.join(models))