# Generated by Django 4.0.4 on 2022-05-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0007_remove_owner_address_owner_cp_owner_downtown_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='apellido paterno'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='second_name',
            field=models.CharField(max_length=30, verbose_name='apellido materno'),
        ),
    ]