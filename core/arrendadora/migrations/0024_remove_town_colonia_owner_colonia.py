# Generated by Django 4.0.4 on 2022-05-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0023_remove_owner_colonia_town_colonia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='town',
            name='colonia',
        ),
        migrations.AddField(
            model_name='owner',
            name='colonia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arrendadora.colonia'),
            preserve_default=False,
        ),
    ]
