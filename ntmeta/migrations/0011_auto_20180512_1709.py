# Generated by Django 2.0.5 on 2018-05-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntmeta', '0010_defaultvalue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultvalue',
            old_name='default',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='defaultvalue',
            name='aspect',
        ),
    ]