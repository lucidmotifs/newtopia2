# meta-System for determining the default value of Entity attribs

class DefaultSystem(object):
    """ Serves to bridge between dynamic attribute association (Aspects)
        and the need to have static and meaningful defaults on a per Entity
        basis.

        There is an indirect link between an aspect.quality.value and an
        Entity. When the default system is run, it creates entries for each
        Entity and all its repsective 'values'? Or, when needed an entry can be
        made in the form: entity :: aspect :: quality :: default """
    pass