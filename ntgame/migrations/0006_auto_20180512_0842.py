# Generated by Django 2.0.5 on 2018-05-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0005_auto_20180512_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rune',
            name='growth_rate',
            field=models.FloatField(default='-5.0'),
        ),
    ]
