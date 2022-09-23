# Generated by Django 4.1.1 on 2022-09-17 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appArbitro', '0002_initial'),
        ('appContrato', '0001_initial'),
        ('appCompeticion', '0001_initial'),
        ('appEquipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('ciudad_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('norma', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='encuentro',
            fields=[
                ('encuentro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('resultado_general', models.CharField(max_length=1)),
                ('resultado_equipo_a', models.IntegerField()),
                ('resultado_equipo_b', models.IntegerField()),
                ('fecha', models.DateField()),
                ('humedad', models.IntegerField()),
                ('clima', models.IntegerField()),
                ('estado_jugado', models.BooleanField()),
                ('equipo_local_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_local_id', to='appEquipo.equipo')),
                ('equipo_visitante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_visitante_id', to='appEquipo.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('estado_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('evento_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('sede_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('capacidad', models.IntegerField()),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPartido.ciudad')),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPartido.estado')),
                ('pais_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais')),
            ],
        ),
        migrations.CreateModel(
            name='evento_persona',
            fields=[
                ('encuentro_evento_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tiempo', models.IntegerField()),
                ('encuentro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro')),
                ('evento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPartido.evento')),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appContrato.persona')),
            ],
        ),
        migrations.AddField(
            model_name='encuentro',
            name='sede_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPartido.sede'),
        ),
        migrations.AddField(
            model_name='encuentro',
            name='terma_arbitral_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appArbitro.terma_arbitral'),
        ),
    ]