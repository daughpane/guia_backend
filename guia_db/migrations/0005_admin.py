# Generated by Django 5.0.1 on 2024-01-26 06:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('admin_username', models.TextField(validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username can only letters, digits, hyphen, and underscore', regex='^[a-zA-Z0-9_-]*$')])),
                ('admin_password', models.CharField()),
                ('museum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia_db.museum', verbose_name='museum id')),
            ],
        ),
    ]
