# Generated by Django 5.0.1 on 2024-02-03 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_db', '0007_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('art_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('medium', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('dimen_width_cm', models.DecimalField(decimal_places=2, max_digits=100)),
                ('dimen_length_cm', models.DecimalField(decimal_places=2, max_digits=100)),
                ('dimen_height_cm', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.TextField()),
                ('additional_info', models.TextField()),
                ('images', models.JSONField(default=list)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guia_db.admin', verbose_name='added by')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='located_artworks', to='guia_db.section', verbose_name='location')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_artworks', to='guia_db.section', verbose_name='section_id')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_artworks', to='guia_db.admin', verbose_name='updated by')),
            ],
        ),
    ]
