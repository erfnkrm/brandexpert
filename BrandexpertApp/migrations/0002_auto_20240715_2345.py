# Generated by Django 3.2.10 on 2024-07-15 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BrandexpertApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='source',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
