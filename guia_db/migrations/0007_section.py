# Generated by Django 5.0.1 on 2024-02-03 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0006_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('section_name', models.TextField()),
                ('museum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia_db.museum', verbose_name='museum_id')),
            ],
        ),
    ]
