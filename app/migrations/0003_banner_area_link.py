# Generated by Django 3.2.10 on 2023-10-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner_area',
            name='link',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]