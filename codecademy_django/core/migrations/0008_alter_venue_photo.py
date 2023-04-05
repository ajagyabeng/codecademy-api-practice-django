# Generated by Django 4.1.6 on 2023-04-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_venue_photo_alter_photo_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='core.photo'),
            preserve_default=False,
        ),
    ]
