# Generated by Django 4.0.4 on 2022-10-16 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id_carrera', models.IntegerField(primary_key=True, serialize=False)),
                ('carrera', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'db_carrera',
            },
        ),
        migrations.CreateModel(
            name='Clase_licencia',
            fields=[
                ('id_clase_licencia', models.IntegerField(primary_key=True, serialize=False)),
                ('clase_licencia', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_clase_licencia',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.IntegerField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'db_color',
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id_conductor', models.IntegerField(primary_key=True, serialize=False)),
                ('num_licencia', models.CharField(max_length=14)),
                ('id_clase_licencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.clase_licencia')),
            ],
            options={
                'db_table': 'db_conductor',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'db_estado',
            },
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id_pasajero', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('appaterno', models.CharField(max_length=40)),
                ('apmaterno', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=14)),
                ('fech_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=50)),
                ('numero_celular', models.CharField(max_length=15)),
                ('calificacion', models.IntegerField()),
                ('imagen_pasajero', models.ImageField(null=True, upload_to='pasajero')),
                ('password', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('id_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.carrera')),
            ],
            options={
                'db_table': 'db_pasajero',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.IntegerField(primary_key=True, serialize=False)),
                ('sede', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'db_sede',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tipo_pago', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'db_tipo_pago',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id_viaje', models.IntegerField(primary_key=True, serialize=False)),
                ('origen', models.CharField(max_length=40)),
                ('destino', models.CharField(max_length=40)),
                ('fech_viaje', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('capacidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=40)),
                ('id_conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.conductor')),
                ('id_pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.pasajero')),
            ],
            options={
                'db_table': 'db_viaje',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo_vehiculo', models.CharField(max_length=40)),
                ('patente', models.CharField(max_length=40)),
                ('imagen_vehiculo', models.ImageField(null=True, upload_to='vehiculo')),
                ('id_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.color')),
                ('id_conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.conductor')),
            ],
            options={
                'db_table': 'db_vehiculo',
            },
        ),
        migrations.AddField(
            model_name='pasajero',
            name='id_sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.sede'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.IntegerField(primary_key=True, serialize=False)),
                ('fech_pago', models.DateField()),
                ('monto', models.IntegerField()),
                ('id_conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.conductor')),
                ('id_pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.pasajero')),
                ('id_viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.viaje')),
            ],
            options={
                'db_table': 'db_pago',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id_historial', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('monto', models.IntegerField()),
                ('origen', models.CharField(max_length=40)),
                ('destino', models.CharField(max_length=40)),
                ('fech_viaje', models.DateField()),
                ('id_conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.conductor')),
                ('id_pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.pasajero')),
                ('id_viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiTeLlevoAPP.viaje')),
            ],
            options={
                'db_table': 'db_historial',
            },
        ),
    ]
