from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from subject.models import subject

# Create your models here.
class nausea(models.Model):
    nauseaid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    trains = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    airplanes = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    smallboats = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    ships = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    swings = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    roundabout = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    funfair = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    busses = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
    cars = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]) 
