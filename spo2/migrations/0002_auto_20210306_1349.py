# Generated by Django 3.1 on 2021-03-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spo2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spo2',
            name='spo2id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
