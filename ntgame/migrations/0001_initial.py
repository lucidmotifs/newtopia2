# Generated by Django 2.0.5 on 2018-05-12 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntmeta', '0009_auto_20180511_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bushel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.IntegerField(default=0)),
                ('name_short', models.CharField(blank=True, max_length=200, null=True)),
                ('name_abbr', models.CharField(blank=True, max_length=200, null=True)),
                ('name_plural', models.CharField(blank=True, max_length=200, null=True)),
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='GoldCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.IntegerField(default=0)),
                ('name_short', models.CharField(blank=True, max_length=200, null=True)),
                ('name_abbr', models.CharField(blank=True, max_length=200, null=True)),
                ('name_plural', models.CharField(blank=True, max_length=200, null=True)),
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Peasant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('growth_rate', models.FloatField(default=0.0)),
                ('amount_total', models.IntegerField(default=0)),
                ('name_short', models.CharField(blank=True, max_length=200, null=True)),
                ('name_abbr', models.CharField(blank=True, max_length=200, null=True)),
                ('name_plural', models.CharField(blank=True, max_length=200, null=True)),
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Province Name')),
                ('ruler', models.CharField(max_length=60, verbose_name='Ruler Name')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.IntegerField(default=0)),
                ('name_short', models.CharField(blank=True, max_length=200, null=True)),
                ('name_abbr', models.CharField(blank=True, max_length=200, null=True)),
                ('name_plural', models.CharField(blank=True, max_length=200, null=True)),
                ('growth_rate', models.FloatField(default=0.0)),
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
                ('province', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province')),
            ],
        ),
        migrations.AddField(
            model_name='peasant',
            name='province',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='province',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
        migrations.AddField(
            model_name='bushel',
            name='province',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ntgame.Province'),
        ),
    ]