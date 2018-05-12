# Province System module
import os
from django.conf import settings

from ntmeta.choices import QualityTypeChoices
from ntmeta.models import Component

COMPONENTS = ('Province', )

GAME_MODEL = 'Province'

DEFAULT_KWARGS_MAP = {
    QualityTypeChoices[0][0]: {
        'max_length': 100,
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
    }
    QualityTypeChoices[4][0]: {}
}

DEFAULT_ARGS_MAP = {
    QualityTypeChoices[4][0]: {"'GoldCoin'"}
}

ENTITY_MODEL_TEMPLATE = """
from django.db import models

class %(name)s(models.Model):
    %(game_model)s = models.OneToOneField('%(game_model_cap)s')
    %(attributes)s

"""

QUALITY_TEMPLATE = """
    %(label)s = %(field)s(%(args)s, %(kwargs)s)
"""

class ProvinceSystem(object):
    """ Province system """

    def __init__(self):
        pass

    @classmethod
    def generate_entities(cls, app):
        # ensure app exists
        assert app in settings.INSTALLED_APPS, 'app not found!'
        # change to app dir
        os.chdir(app+'/models')
        # for each entity assigned to COMPONENTS: ...
        com = Component.objects.filter(name=COMPONENTS[0])
        entities = com[0].assigned.all()
        attributes = []
        for e in entities:
            print(e.id)
            # get aspect qualities
            a_set = e.aspect_set.all()
            for a in a_set:
                # create an attribute for each quality
                for q in a.qualities.all():
                    label = a.name.lower() if (
                        a.name == q.name) else '%s_%s' % (a.name, q.name)
                    print(label)
                    field = q.data_type
                    args = DEFAULT_ARGS_MAP.get(field)
                    kwargs = DEFAULT_KWARGS_MAP.get(field)

                    attributes.append(QUALITY_TEMPLATE % {
                        'label': label,
                        'field': field,
                        'args': *args,
                        'kwargs': **kwargs,
                    })

        print(attributes)

        # with open(GAME_MODEL.lower()+'.py', 'w') as model:
        # build attribute string from aspect qualities (+ \n)

        # i.e. aspect.quality.label = aspect.quality.data_type(DATA_TYPE_TEMPLATE)
        #
        # create inital template string with replacements (including attributes)
        # write file
        # save file
        #
        # for any existing instances of the releated GAMEMODEL, create an instance of
        # model and attach

        print('Done!')  # TODO real logging output
