# Province System module
import os
from django.conf import settings

COMPONENTS = ('Infrastructure', )

GAME_MODEL = 'Infrastructure'

BUFFER_LINE = '### Entity Generation'


class InfrastructureSystem(object):

    def __init__(self):
        pass