from django.db.models import fields
from django.db.models.fields.related import ForeignKey


QualityTypeChoices = (
    (fields.CharField.__name__, 'Text'),
    (fields.IntegerField.__name__, 'Number'),
    (fields.FloatField.__name__, 'Float'),
    (fields.BooleanField.__name__, 'Bool'),
    (ForeignKey.__name__, 'Entity'),
)