# Generated by Django 4.2.5 on 2023-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_rename_desk_listproduct_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/src/img'),
        ),
    ]
