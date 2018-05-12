from ntmeta.systems.base import System
from ntmeta.systems.base import DEFAULT_ARGS_MAP, DEFAULT_KWARGS_MAP

class MilitarySystem(System):
    """ Military system """

    def __init__(self):
        pass

    @classmethod
    def boot(cls, app):
        """ Start the app from scratch, generating Entities and other 
            objects """
        cls.set_core_component('Military')
        cls.set_game_model('Military')

        # generate Entities
        cls.generate_entities(app, DEFAULT_ARGS_MAP, DEFAULT_KWARGS_MAP)

    @classmethod
    def make_entity_instances(cls, app, model):
        """ Create an instance of all related entities and attach to
            `province` """
        for e in cls.get_entities():
            class_ = getattr(app + '.' + cls.game_model.lower(), e.name)
            inst = class_()
            if inst.hasattr('entity'):
                inst.setattr('entity', e)
            # will error if exists (one2one rel) so just try catch pass
            inst.add(model)
            inst.save()

        print('Finished Instatiating Entities')