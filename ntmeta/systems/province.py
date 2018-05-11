# Province System module
import os
from django.conf import settings

from ntmeta.models import Component

COMPONENTS = ('Province', )

GAME_MODEL = 'Province'

ENTITY_MODEL_TEMPLATE = """
from django.db import models

class %(name)s(models.Model):
    %(game_model)s = models.OneToOneField('%(game_model_cap)s')
    %(attributes)s

"""

QUALITY_TEMPLATE = """
    %(label)s = %(field)s(%(kwargs)s)
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
            print(e.aspect_set.all())

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
