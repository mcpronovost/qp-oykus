# Generated by Django 4.1.2 on 2022-10-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpcharacter',
            name='resistance_physical',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Physical Resistance'),
        ),
    ]
