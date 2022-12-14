# Generated by Django 4.1.2 on 2022-10-30 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_alter_qpcharactercurrency_character'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qpcharactercurrency',
            name='amount',
        ),
        migrations.AddField(
            model_name='qpcharactercurrency',
            name='amount_max',
            field=models.IntegerField(default=0, verbose_name='Max Amount'),
        ),
        migrations.AddField(
            model_name='qpcharactercurrency',
            name='amount_min',
            field=models.IntegerField(default=0, verbose_name='Min Amount'),
        ),
    ]
