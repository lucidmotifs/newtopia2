import os

from django.core.management.base import BaseCommand
from django.conf import settings

from ntmeta.choices import QualityType, QualityTypeChoices
from ntmeta.models import DefaultValue
from ntmeta.models import Entity
from ntmeta.models import Quality
from ntmeta.systems.province import ProvinceSystem
from ntmeta.systems.military import MilitarySystem

DEFAULT_VALUES_MAP = {
    QualityType.TEXT: '',
    'IntegerField': 0,
    QualityType.BOOL: True,
    QualityType.FLOAT: 0.0,
    QualityType.ENTITY: Entity.objects.all()[0]
}


class Command(BaseCommand):
    help = 'Creates entity models in specified app'

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='+', type=str)

    def handle(self, *args, **options):

        def read_buffer(file, terminate_at):
            buffer = []
            try:
                with open(file, 'r') as f:
                    for line in f:
                        buffer.append(line)
                        if terminate_at in line:
                            return buffer
            except FileNotFoundError:
                open(file, 'w')
                return read_buffer(file, terminate_at)
            return list()

        def gen_game_model(entity, attributes):
            return Entity.CLASS_TEMPLATE.format(**{
                'name': entity.name.replace(' ', ''),
                'id': entity.id,
                'attributes': '\n    '.join(attributes),
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
                    args.append('\'{}\''.format(q.description.replace("'", '\'')
                
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
                    kwargs['default'] = '\'{}\''.format(default.value)
                except DefaultValue.DoesNotExist:
                    kwargs['default'] = DEFAULT_VALUES_MAP.get(q.data_type)

                attr = Quality.FIELD_TEMPLATE.format(
                    label=label, field=field, args=', '.join(args),
                    kwargs=', '.join(
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
            attributes = []
            for a in e.aspect_set.all():
                fields = gen_attr_fields(e, a)
                attributes.append('\n'.join(fields))
            models.append(gen_game_model(e, attributes))

        buffer = read_buffer('entities.py', '---')
        with open('entities.py', 'w+') as f:
            f.writelines(buffer)
            f.write('\n\n\n'.join(models))
            f.write('\n')

        print('\n\n\n'.join(models))