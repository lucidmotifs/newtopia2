from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ntmeta.systems.province import ProvinceSystem
from ntmeta.systems.military import MilitarySystem

class GenerateEntities(BaseCommand):
    help = 'Creates entity models in specified app'

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='+', type=str)

    def handle(self, *args, **options):
        app = options['app']
        assert app in settings.INSTALLED_APPS, 'app not found'

        # move to models directory of `app`
        os.chdir(app+'/models')

        