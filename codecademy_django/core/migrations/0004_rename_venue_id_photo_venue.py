# Generated by Django 4.1.7 on 2023-03-30 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_venue_photo_photo_venue_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='venue_id',
            new_name='venue',
        ),
    ]