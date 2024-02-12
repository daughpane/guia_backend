# Generated by Django 4.0 on 2024-02-11 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('guia_db', '0014_remove_admin_admin_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='admin_id',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='location',
        ),
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='date_published',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='dimen_height_cm',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
    ]
