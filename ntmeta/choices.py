from enum import Enum

from django.db.models import fields
from django.db.models.fields.related import ForeignKey

# TODO move ot seperate module
class QualityType(Enum):
    TEXT = 'Text'
    NUMBER = 'Number'
    FLOAT = 'Float'
    BOOL = 'Bool'
    ENTITY = 'Entity'


QualityTypeChoices = (
    (fields.CharField.__name__, QualityType.TEXT),
    (fields.IntegerField.__name__, QualityType.NUMBER),
    (fields.FloatField.__name__, QualityType.FLOAT),
    (fields.BooleanField.__name__, QualityType.BOOL),
    (ForeignKey.__name__, QualityType.ENTITY),
)