# Generated by Django 4.0.4 on 2022-05-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0041_alter_unidad_plazo_delete_plazos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.conceptos')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendadora.unidad')),
            ],
        ),
    ]