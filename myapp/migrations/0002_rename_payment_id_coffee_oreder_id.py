# Generated by Django 5.0.6 on 2024-07-06 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='payment_id',
            new_name='oreder_id',
        ),
    ]
