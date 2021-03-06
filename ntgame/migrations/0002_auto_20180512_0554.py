# Generated by Django 2.0.5 on 2018-05-12 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushel',
            name='entity',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity'),
        ),
        migrations.AlterField(
            model_name='bushel',
            name='province',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
        migrations.AlterField(
            model_name='goldcoin',
            name='entity',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity'),
        ),
        migrations.AlterField(
            model_name='goldcoin',
            name='province',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
        migrations.AlterField(
            model_name='peasant',
            name='entity',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity'),
        ),
        migrations.AlterField(
            model_name='peasant',
            name='province',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
        migrations.AlterField(
            model_name='rune',
            name='entity',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity'),
        ),
        migrations.AlterField(
            model_name='rune',
            name='province',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
    ]
