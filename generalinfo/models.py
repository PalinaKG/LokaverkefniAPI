from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from subject.models import subject

# Create your models here.
class generalinfo(models.Model):
    genid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    foodtime = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    caffeine = models.IntegerField(validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]) 
    weight = models.IntegerField() 
    healthyscale = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]) 
    groups = models.CharField(max_length=20) 
    nicotine = models.IntegerField(validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]) 
    noexercise = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    alcohol = models.IntegerField(validators=[
            MaxValueValidator(2),
            MinValueValidator(0)
        ]) 
    msdrugs = models.IntegerField(validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]) 
    motionsickness = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    comments = models.CharField(max_length=100) 
