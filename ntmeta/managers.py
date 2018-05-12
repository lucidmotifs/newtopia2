from ntmeta.models import Entity, DefaultValue

class EntityManager(object):
    
    @classmethod
    def get_default_values(cls, entity):
        qs = DefaultValue.objects.filter(entity=entity)
        return {r.quality.label: r.value for r in qs}


    @classmethod
    def get_quality_list(cls, entity):
        """ return a list of all qualities related to a given entity """
        ret = []
        for asp in entity.aspect_set.all():
            ret.extend(asp.quality_set.all())
        return ret
