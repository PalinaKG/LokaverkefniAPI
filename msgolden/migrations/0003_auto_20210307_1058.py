# Generated by Django 3.1 on 2021-03-07 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgolden', '0002_auto_20210306_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgolden',
            name='blurredvision',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='diffoffocus',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='dizziness',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='eyestrain',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='fatigue',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='gendiscomfort',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='headache',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='incrsalvation',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='nausea',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='sweat',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='msgolden',
            name='type',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
    ]
