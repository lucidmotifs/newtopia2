# django modules
from django.db import models
from ntgame.models.province import Province


class Science(models.Model):

    province = models.OneToOneField(
        Province, null=False, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'Science Models'