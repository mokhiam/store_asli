# Generated by Django 3.2.9 on 2022-02-22 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220221_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='Price',
            new_name='price',
        ),
    ]
