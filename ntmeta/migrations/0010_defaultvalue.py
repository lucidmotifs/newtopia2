# Generated by Django 2.0.5 on 2018-05-12 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntmeta', '0009_auto_20180511_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.CharField(blank=True, max_length=200, null=True)),
                ('aspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Aspect')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Entity')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntmeta.Quality')),
            ],
        ),
    ]
