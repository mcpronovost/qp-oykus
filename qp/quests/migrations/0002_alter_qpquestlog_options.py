# Generated by Django 4.1.2 on 2022-10-29 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qpquestlog',
            options={'ordering': ['-start'], 'verbose_name': 'Quest Log', 'verbose_name_plural': 'Quest Logs'},
        ),
    ]
