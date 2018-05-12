# Province System module
import os
from django.conf import settings

from ntmeta.choices import QualityTypeChoices
from ntmeta.managers import EntityManager
from ntmeta.models import Component, DefaultValue
from ntmeta.systems.default import DefaultSystem

COMPONENTS = ('Province', )

GAME_MODEL = 'Province'

BUFFER_LINE = '### Entity Generation'

DEFAULT_KWARGS_MAP = {
    QualityTypeChoices[0][0]: {
        'max_length': 200,
        'null': True,
        'blank': True,
    },
    QualityTypeChoices[1][0]: {
        'default': 0,
    },
    QualityTypeChoices[2][0]: {
        'default': 0.0,
    },
    QualityTypeChoices[3][0]: {
        'blank': False,
        'default': True,
    },
    QualityTypeChoices[4][0]: {}
}

DEFAULT_ARGS_MAP = {
    QualityTypeChoices[4][0]: {"'GoldCoin'"}
}

ENTITY_MODEL_TEMPLATE = \
"""
class %(name)s(models.Model):
    entity = models.OneToOneField(
        'ntmeta.Entity', on_delete=models.CASCADE, default=%(entity_id)s)
    %(game_model)s = models.OneToOneField(
        '%(game_model_cap)s', on_delete=models.CASCADE, blank=True)
%(attributes)s
"""

QUALITY_TEMPLATE = \
"""    %(label)s = %(field)s(%(args)s%(kwargs)s)
"""


class ProvinceSystem(object):
    """ Province system """

    def __init__(self):
        pass

    @classmethod
    def buffer_game_model(cls):
        buffer = []
        with open(GAME_MODEL.lower()+'.py', 'r') as f:
            for line in f:
                buffer.append(line)
                if "###" in line:
                    return buffer                

        return buffer

    @classmethod
    def get_entities(cls):
        """ Code could live on Component module """
        com = Component.objects.filter(name=COMPONENTS[0])
        return com[0].assigned.all()


    @classmethod
    def generate_entities(cls, app):
        # ensure app exists
        assert app in settings.INSTALLED_APPS, 'app not found!'
        # change to app dir
        os.chdir(app+'/models')
        buffer = cls.buffer_game_model()
        
        models, attributes = {}, {}
        # TODO abstract attribute generation to EntityManager.build_attribs(e)
        for e in cls.get_entities():
            attributes[e.id] = []
            e_attrib = attributes[e.id]
            
            # get aspect qualities
            a_set = e.aspect_set.all()
            for a in a_set:
                # create an attribute for each quality
                for q in a.quality_set.all():
                    label = a.name.lower() if (
                        a.name.lower() == q.label) else '%s_%s' % (
                            a.name.lower(), q.label)

                    field = 'models.{}'.format(q.data_type)

                    args = DEFAULT_ARGS_MAP.get(q.data_type, ())
                    kwargs = DEFAULT_KWARGS_MAP.get(q.data_type, {}).copy()                  

                    # check for a default value
                    try:
                        default = DefaultValue.objects.get(
                            entity=e, aspect=a, quality=q)
                        kwargs['default'] = "'{}'".format(default.default)
                    except DefaultValue.DoesNotExist:
                        pass

                    arg_string = ', '.join(args) + ', ' if len(args) else ''
                    kwargs_string = ', '.join(
                        ['%s=%s' % (k, v) for k, v in kwargs.items()])
                    e_attrib.append(QUALITY_TEMPLATE % {
                        'label': label,
                        'field': field,
                        'args': arg_string,
                        'kwargs': kwargs_string,
                    })
            # create inital template string with replacements
            # (including attributes)
            models[e.name] = ENTITY_MODEL_TEMPLATE % {
                'name': e.name.title().replace(' ', ''),
                'game_model': GAME_MODEL.lower(),
                'game_model_cap': GAME_MODEL.capitalize(),
                'entity_id': e.id,
                'attributes': ''.join(attributes[e.id]),
            }
        # [print(m) for m in models.values()]

        with open(GAME_MODEL.lower()+'.py', 'w') as f:
            # write file
            f.writelines(buffer)
            [f.write(model) for model in models.values()]

        # for any existing instances of the releated GAMEMODEL
        # then create an instance of model and attach it

        print('Finished Generating Entites')  # TODO real logging output

        # return [m for m in models.values()]

    @classmethod
    def make_entity_instances(cls, app, model):
        """ Create an instance of all related entities and attach to
            `province` """
        for e in cls.get_entities():
            class_ = getattr(app + '.' + GAME_MODEL.lower(), e.name)
            inst = class_()
            if inst.hasattr('entity'):
                inst.setattr('entity', e)
            # will error if exists (one2one rel) so just try catch pass
            inst.add(model)
            inst.save()

        print('Finished Instatiating Entities')
        
