# Generated by Django 4.0.4 on 2022-05-09 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrendadora.address'),
        ),
    ]