# Generated by Django 4.1.2 on 2022-10-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0007_qpsettingsrpg_quest_malus_level_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpsettingsrpg',
            name='total_attribute',
            field=models.PositiveSmallIntegerField(default=6, verbose_name='Total Attribute'),
        ),
    ]