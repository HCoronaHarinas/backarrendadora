# Generated by Django 4.0.4 on 2022-06-01 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0011_register_comentarios_register_referencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='unidad',
        ),
    ]