# Generated by Django 5.0.6 on 2024-07-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]