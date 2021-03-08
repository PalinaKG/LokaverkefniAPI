from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from subject.models import subject

# Create your models here.
class msgolden(models.Model):
    msgoldenid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    type = models.IntegerField(validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]) 
    dizziness = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    nausea = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    sweat = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    diffoffocus = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    blurredvision = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    incrsalvation = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    eyestrain = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    headache = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    fatigue = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 
    gendiscomfort = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ]) 

