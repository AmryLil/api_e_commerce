# Generated by Django 4.2.5 on 2023-12-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_datasellers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasellers',
            name='current_user',
            field=models.CharField(max_length=255),
        ),
    ]
