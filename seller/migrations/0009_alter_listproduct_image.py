# Generated by Django 4.2.5 on 2023-11-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_alter_listproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listproduct',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/src/img'),
        ),
    ]
