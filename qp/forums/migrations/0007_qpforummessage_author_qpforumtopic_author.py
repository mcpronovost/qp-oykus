# Generated by Django 4.1.2 on 2022-11-01 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_remove_qpcharactercurrency_amount_max_and_more'),
        ('forums', '0006_qpforumcategory_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpforummessage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='characters.qpcharacter', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='qpforumtopic',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topics', to='characters.qpcharacter', verbose_name='Author'),
        ),
    ]
