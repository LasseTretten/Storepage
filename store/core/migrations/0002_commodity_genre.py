# Generated by Django 4.1.6 on 2023-02-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.genre'),
        ),
    ]
