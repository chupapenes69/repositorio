# Generated by Django 4.1.1 on 2022-09-22 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0004_alter_competicion_options_alter_deporte_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicion',
            name='pais_id',
            field=models.ForeignKey(db_column='pais_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais'),
        ),
    ]
