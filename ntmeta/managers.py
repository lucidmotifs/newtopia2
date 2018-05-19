from ntmeta.models import Entity, DefaultValue

class EntityManager(object):
    
    @classmethod
    def get_default_values(cls, entity):
        qs = DefaultValue.objects.filter(entity=entity)
        return {r.quality.label: r.value for r in qs}


    @classmethod
    def get_quality_list(cls, entity):
        """ return a list of all qualities related to a given entity """
        ret = {}
        for a in entity.aspect_set.all():
            ret.extend({a.name.lower(): a.quality_set.all()})
        return ret


    @classmethod
    def build_attribs(cls, entity, defaults):
        for a, q in cls.get_quality_list(entity).items():
            label = a.name.lower() if (
                a.name.lower() == q.label) else '%s_%s' % (
                    a.name.lower().replace(' ', '_'), q.label)

            field = 'models.{}'.format(q.data_type)
