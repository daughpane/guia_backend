# Generated by Django 4.0 on 2024-03-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0002_visitor_museum_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='updated_on',
            field=models.DateTimeField(),
        ),
    ]
