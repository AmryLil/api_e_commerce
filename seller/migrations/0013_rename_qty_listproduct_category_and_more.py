# Generated by Django 4.2.5 on 2023-12-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_listproduct_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listproduct',
            old_name='qty',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='listproduct',
            old_name='type',
            new_name='stock',
        ),
        migrations.AlterField(
            model_name='listproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
