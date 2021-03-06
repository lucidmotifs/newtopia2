# Generated by Django 2.0.5 on 2018-05-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntmeta', '0010_defaultvalue'),
        ('ntgame', '0009_auto_20180512_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefensiveSpecialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defensive_strength_value', models.IntegerField(default=0)),
                ('amount_total', models.IntegerField(default=0)),
                ('entity', models.OneToOneField(default=8, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Elite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offensive_strength_value', models.IntegerField(default=0)),
                ('defensive_strength_value', models.IntegerField(default=0)),
                ('amount_total', models.IntegerField(default=0)),
                ('cost_price', models.IntegerField(default=0)),
                ('cost_scaling', models.FloatField(default=0.0)),
                ('cost_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntgame.GoldCoin')),
                ('entity', models.OneToOneField(default=9, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Military',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province')),
            ],
        ),
        migrations.CreateModel(
            name='OffensiveSpecialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offensive_strength_value', models.IntegerField(default=0)),
                ('amount_total', models.IntegerField(default=0)),
                ('entity', models.OneToOneField(default=7, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
                ('military', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Military')),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.IntegerField(default=0)),
                ('offensive_strength_value', models.IntegerField(default=0)),
                ('defensive_strength_value', models.IntegerField(default=0)),
                ('consumes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntgame.GoldCoin')),
                ('entity', models.OneToOneField(default=6, on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
                ('military', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Military')),
            ],
        ),
        migrations.AddField(
            model_name='elite',
            name='military',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Military'),
        ),
        migrations.AddField(
            model_name='defensivespecialist',
            name='military',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Military'),
        ),
    ]
