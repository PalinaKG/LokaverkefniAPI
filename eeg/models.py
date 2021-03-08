from django.db import models
from subject.models import subject
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class eeg(models.Model):
    eegid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    alpha = models.DecimalField(max_digits=15, decimal_places=8)
    beta = models.DecimalField(max_digits=15, decimal_places=8)
    theta = models.DecimalField(max_digits=15, decimal_places=8)
    low_gamma = models.DecimalField(max_digits=15, decimal_places=8)
    delta = models.DecimalField(max_digits=15, decimal_places=8)
    interval = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0)])
    sensor = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0)])