# Generated by Django 4.1.2 on 2022-10-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0002_alter_qpquestlog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpquestlog',
            name='reward_exp',
            field=models.PositiveIntegerField(default=1, verbose_name='Reward Experience'),
        ),
    ]