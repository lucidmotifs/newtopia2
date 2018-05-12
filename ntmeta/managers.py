# TODO just remove all this shit...
SHORT_MAP = {
    'Bushel': 'Food',
    'Gold Coin': 'Money',
}

PLURAL_MAP = {

}

class EntityManager(object):
    
    @classmethod
    def get_name_defaults(cls, entity):
        print('getting defaults for entity: %s' % entity.name)
        # TODO move these statically type defaults to meta db
        # TODO manage this via an Aspect class for Name
        space_split = entity.name.split(' ')
        if len(space_split) > 1:
            # abbr is first letter of each word
            abbr = ''
            for word in space_split:
                abbr += word[0].lower()
        else:
            abbr = None

        return {
            'short': SHORT_MAP.get(entity.name),
            'plural': PLURAL_MAP.get(entity.name),
            'abbr': abbr,
        }