# Generated by Django 3.1.5 on 2021-01-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_rating', '0004_auto_20210107_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='restaurant name'),
        ),
    ]
