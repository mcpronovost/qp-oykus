# Generated by Django 4.1.2 on 2022-10-31 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0010_qpsettingsrpg_limit_inventory_size_character_and_more'),
        ('forums', '0003_alter_qpforum_rpg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qpforumtopic',
            options={'ordering': ['-flag', '-updated_at'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.AlterField(
            model_name='qpforum',
            name='rpg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='forum', to='rpg.qprpg'),
        ),
    ]
