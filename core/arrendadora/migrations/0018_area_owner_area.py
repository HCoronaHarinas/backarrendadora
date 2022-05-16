# Generated by Django 4.0.4 on 2022-05-10 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrendadora', '0017_town_remove_owner_downtown_owner_town'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Area')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arrendadora.area'),
            preserve_default=False,
        ),
    ]