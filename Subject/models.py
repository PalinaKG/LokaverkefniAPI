from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class subject(models.Model):
    subjectid = models.IntegerField(primary_key=True, default=1)
    height = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
    gender = models.IntegerField(validators=[
            MaxValueValidator(0),
            MinValueValidator(2)
        ])
    handedness = models.IntegerField(validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    birthyear = models.IntegerField(validators=[
            MaxValueValidator(2021),
        ])


    # def __str__(self):
    #     return self.height