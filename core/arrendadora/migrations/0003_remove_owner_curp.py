# Generated by Django 4.0.4 on 2022-05-20 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0002_alter_owner_apodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='curp',
        ),
    ]