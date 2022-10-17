# Generated by Django 4.1.1 on 2022-10-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_qpuserprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpuserprofile',
            name='timezone',
            field=models.CharField(choices=[('America/Toronto', 'America/Toronto'), ('Europe/Paris', 'Europe/Paris')], default='America/Toronto', max_length=32, verbose_name='Timezone'),
        ),
    ]
