# Generated by Django 3.2.10 on 2023-10-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Pic/banner')),
                ('discount_del', models.CharField(max_length=100)),
                ('quet', models.CharField(max_length=100)),
                ('dicount', models.IntegerField()),
            ],
        ),
    ]