# Generated by Django 4.1.6 on 2023-04-04 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_venue_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='core.photo'),
        ),
    ]
