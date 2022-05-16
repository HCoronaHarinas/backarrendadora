# Generated by Django 4.0.4 on 2022-05-10 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0044_estadodecuenta_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.PositiveIntegerField(default=0, verbose_name='importe')),
                ('fecha', models.DateField(auto_now=True, verbose_name='fecha')),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.conceptos', verbose_name='concepto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner', verbose_name='tipo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.tipo', verbose_name='tipo')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.unidad', verbose_name='unidad')),
            ],
        ),
    ]