# Generated by Django 4.1.2 on 2022-10-30 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0004_remove_qpquestlog_reward_exp_qpquest_reward_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpquest',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=30), verbose_name='Duration'),
        ),
    ]
