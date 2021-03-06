# Generated by Django 4.0.4 on 2022-05-20 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Colonia')),
            ],
        ),
        migrations.CreateModel(
            name='Conceptos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Concepto')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Año')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('first_name', models.CharField(max_length=30, verbose_name='apellido paterno')),
                ('second_name', models.CharField(max_length=30, verbose_name='apellido materno')),
                ('apodo', models.CharField(max_length=30, null=True, verbose_name='apodo')),
                ('curp', models.CharField(max_length=18, unique=True, verbose_name='curp')),
                ('rfc', models.CharField(max_length=13, unique=True, verbose_name='rfc')),
                ('mail', models.EmailField(max_length=254, unique=True, verbose_name='correo')),
                ('cp', models.PositiveIntegerField(verbose_name='cp')),
                ('street', models.CharField(max_length=200, verbose_name='calle')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='numero')),
                ('interior', models.PositiveIntegerField(null=True, verbose_name='interior')),
                ('date_create', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.colonia')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Estatus')),
            ],
        ),
        migrations.CreateModel(
            name='Submarca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Submarca')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Alcaldia')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.PositiveIntegerField(unique=True, verbose_name='Numero de unidad')),
                ('placas', models.CharField(max_length=50, verbose_name='Placas')),
                ('valor', models.FloatField(verbose_name='Valor Factura')),
                ('tasa', models.FloatField(verbose_name='Tasa')),
                ('plazo', models.PositiveIntegerField(verbose_name='Plazo')),
                ('tiie', models.FloatField(verbose_name='TIIE')),
                ('date_create', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.marca')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.status')),
                ('submarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.submarca')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.PositiveIntegerField(default=0, verbose_name='importe')),
                ('fecha', models.DateField(auto_now=True, verbose_name='fecha')),
                ('date_update', models.DateField(auto_now_add=True)),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.conceptos', verbose_name='concepto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner', verbose_name='propietario')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.tipo', verbose_name='tipo')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.unidad', verbose_name='unidad')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.status'),
        ),
        migrations.AddField(
            model_name='owner',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.town'),
        ),
        migrations.AddField(
            model_name='marca',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.modelo'),
        ),
        migrations.AddField(
            model_name='marca',
            name='submarca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.submarca'),
        ),
        migrations.AddField(
            model_name='conceptos',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.tipo'),
        ),
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150, verbose_name='ref')),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.conceptos')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.unidad')),
            ],
        ),
    ]
