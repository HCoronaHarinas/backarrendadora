# Generated by Django 4.0.4 on 2022-05-10 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0030_remove_unidad_modelo_alter_modelo_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidad',
            name='name',
        ),
    ]
