# Generated by Django 4.1.2 on 2022-10-30 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0006_qpquestrewardcurrency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qpquestrewardcurrency',
            name='amount',
        ),
        migrations.AddField(
            model_name='qpquestrewardcurrency',
            name='amount_max',
            field=models.IntegerField(default=0, verbose_name='Max Amount'),
        ),
        migrations.AddField(
            model_name='qpquestrewardcurrency',
            name='amount_min',
            field=models.IntegerField(default=0, verbose_name='Min Amount'),
        ),
    ]
