# Generated by Django 3.1.5 on 2021-01-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='restaurant_images'),
        ),
    ]