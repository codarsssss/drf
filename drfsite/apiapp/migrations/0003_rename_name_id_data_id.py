# Generated by Django 4.2.1 on 2023-05-07 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_rename_id_data_name_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='name_id',
            new_name='id',
        ),
    ]