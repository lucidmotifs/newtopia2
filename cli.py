import sys, os
from importlib import import_module
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'newtopia.settings'
django.setup()
# django configured, can import models etc.

from ntmeta.systems.province import ProvinceSystem
from ntmeta.systems.province import GAME_MODEL as ProvinceModel

if __name__ == '__main__':
    # TODO app from args (argsparse in general)
    ProvinceSystem.generate_entities('ntgame')

    # get model class
    module = import_module('ntgame.models.{}'.format(ProvinceModel.lower()))
    m = getattr(module, ProvinceModel)
    
    # attach entities to all existing models
    # for obj in m.objects.all():
        # ProvinceSystem.make_entity_instances('ntgame', obj)

    print('CLI task complete')

