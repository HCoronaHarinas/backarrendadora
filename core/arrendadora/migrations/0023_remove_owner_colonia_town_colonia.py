# Generated by Django 4.0.4 on 2022-05-10 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0022_remove_owner_area_delete_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='colonia',
        ),
        migrations.AddField(
            model_name='town',
            name='colonia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arrendadora.colonia'),
            preserve_default=False,
        ),
    ]
