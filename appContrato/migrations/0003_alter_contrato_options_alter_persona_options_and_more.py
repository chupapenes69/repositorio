# Generated by Django 4.1.1 on 2022-09-19 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0002_alter_contrato_persona_id_alter_persona_pais_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contrato',
            options={'verbose_name_plural': 'contrato'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name_plural': 'persona'},
        ),
        migrations.AlterModelOptions(
            name='tipo_persona',
            options={'verbose_name_plural': 'tipo_persona'},
        ),
    ]
