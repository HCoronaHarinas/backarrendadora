# Generated by Django 4.0.4 on 2022-05-10 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0035_remove_owner_unidad_owner_unidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='unidad',
        ),
        migrations.AddField(
            model_name='unidad',
            name='propietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arrendadora.owner'),
            preserve_default=False,
        ),
    ]