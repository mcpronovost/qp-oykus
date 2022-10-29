# Generated by Django 4.1.2 on 2022-10-29 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0005_alter_qprpgskill_attribute'),
        ('characters', '0003_qpcharacter_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpcharacter',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to='rpg.qprpgrace', verbose_name='Race'),
        ),
    ]
