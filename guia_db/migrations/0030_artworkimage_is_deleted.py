# Generated by Django 4.0 on 2024-02-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0029_alter_artwork_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkimage',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
