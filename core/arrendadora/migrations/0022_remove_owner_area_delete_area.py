# Generated by Django 4.0.4 on 2022-05-10 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0021_remove_owner_suburb_delete_suburb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='area',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]