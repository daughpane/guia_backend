# Generated by Django 4.0 on 2024-03-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0003_alter_artwork_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),
    ]
