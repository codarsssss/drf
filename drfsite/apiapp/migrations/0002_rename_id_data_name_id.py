# Generated by Django 4.2.1 on 2023-05-07 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='id',
            new_name='name_id',
        ),
    ]
