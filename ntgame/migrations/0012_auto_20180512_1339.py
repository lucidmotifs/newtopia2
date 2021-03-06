# Generated by Django 2.0.5 on 2018-05-12 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0011_auto_20180512_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elite',
            name='cost_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_paid', to='ntmeta.Entity'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='consumes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumes_entity', to='ntmeta.Entity'),
        ),
    ]
