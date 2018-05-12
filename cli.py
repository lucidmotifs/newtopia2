import sys, os
from importlib import import_module
import django

from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = 'newtopia.settings'
django.setup()
# django configured, can import models etc.

from ntmeta.systems.province import ProvinceSystem
from ntmeta.systems.military import MilitarySystem

if __name__ == '__main__':
    app = 'ntgame'
    assert app in settings.INSTALLED_APPS, 'app not found!'
    os.chdir(app+'/models')

    # TODO app from args (argsparse in general)
    ProvinceSystem.boot(app)
    # get model class
    module = import_module(
        'ntgame.models.{}'.format(ProvinceSystem.game_model.lower()))
    m = getattr(module, ProvinceSystem.game_model)
    print(m)
    print('Province System running')

    MilitarySystem.boot(app)
    # get model class ...
    
    # attach entities to all existing models
    # for obj in m.objects.all():
        # ProvinceSystem.make_entity_instances('ntgame', obj)

    print('CLI task complete')

