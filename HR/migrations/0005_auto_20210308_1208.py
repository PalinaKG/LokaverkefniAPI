# Generated by Django 3.1 on 2021-03-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_auto_20210307_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='time',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]