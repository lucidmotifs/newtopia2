# Base Class for Systems
import os

from ntmeta.choices import QualityTypeChoices
from ntmeta.models import Component, DefaultValue

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
    QualityTypeChoices[4][0]: {
        'on_delete': 'models.CASCADE',
    }
}

DEFAULT_ARGS_MAP = {
    QualityTypeChoices[4][0]: {"'ntmeta.Entity'"}
}

class System(object):

    tpl_entity_model = \
"""
class %(name)s(models.Model):
    entity = models.ForeignKey(
        'ntmeta.Entity', on_delete=models.CASCADE, default=%(entity_id)s)
    %(game_model)s = models.OneToOneField(
        '%(game_model_cap)s', on_delete=models.CASCADE, blank=True)
%(attributes)s
"""

    tpl_quality = \
"""    %(label)s = %(field)s(%(args)s%(kwargs)s)
"""

    @classmethod
    def set_game_model(cls, game_model):
        cls.game_model = game_model

    @classmethod
    def set_core_component(cls, component_name):
        cls.core_component = component_name

    @classmethod
    def get_entities(cls):
        """ Code could live on Component module """
        com = Component.objects.get(name=cls.core_component)
        return com.assigned.all()

    @classmethod
    def buffer_game_model(cls):
        buffer = []
        with open(cls.game_model.lower()+'.py', 'r') as f:
            for line in f:
                buffer.append(line)
                if "###" in line:
                    return buffer                

        return buffer

    @classmethod
    def generate_entities(cls, app, args_map, kwargs_map):
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
                            a.name.lower().replace(' ', '_'), q.label)

                    field = 'models.{}'.format(q.data_type)

                    args = args_map.get(q.data_type, ())
                    kwargs = kwargs_map.get(q.data_type, {}).copy()

                    # check for a default value
                    try:
                        default = DefaultValue.objects.get(
                            entity=e, quality=q)
                        kwargs['default'] = "'{}'".format(default.default)
                    except DefaultValue.DoesNotExist:
                        pass

                    arg_string = ', '.join(args) + ', ' if len(args) else ''
                    kwargs_string = ', '.join(
                        ['%s=%s' % (k, v) for k, v in kwargs.items()])
                    e_attrib.append(cls.tpl_quality % {
                        'label': label,
                        'field': field,
                        'args': arg_string,
                        'kwargs': kwargs_string,
                    })
            # create inital template string with replacements
            # (including attributes)
            models[e.name] = cls.tpl_entity_model % {
                'name': e.name.title().replace(' ', ''),
                'game_model': cls.game_model.lower(),
                'game_model_cap': cls.game_model.capitalize(),
                'entity_id': e.id,
                'attributes': ''.join(attributes[e.id]),
            }
        # [print(m) for m in models.values()]

        with open(cls.game_model.lower()+'.py', 'w') as f:
            # write file
            f.writelines(buffer)
            [f.write(model) for model in models.values()]

        # for any existing instances of the releated GAMEMODEL
        # then create an instance of model and attach it

        print('Finished Generating Entites')  # TODO real logging output

        # return [m for m in models.values()]