# Generated by Django 4.1.1 on 2022-10-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_qpuserprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpuserprofile',
            name='limit_max_projects',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='Max Projects'),
        ),
    ]
