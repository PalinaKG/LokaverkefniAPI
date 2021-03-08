from django.db import models
from subject.models import subject
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class hr(models.Model):
    hrid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    bpm = models.DecimalField(max_digits=10, decimal_places=4) 
    interval = models.IntegerField(default = 0, validators=[MaxValueValidator(6), MinValueValidator(1)])