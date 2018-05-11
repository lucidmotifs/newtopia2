import sys, os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'newtopia.settings'
django.setup()
# django configured, can import models etc.

from ntmeta.systems.province import ProvinceSystem

if __name__ == '__main__':
    # TODO app from args (argsparse in general)
    ProvinceSystem.generate_entities('ntgame')

