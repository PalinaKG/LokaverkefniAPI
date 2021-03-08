from django.db import models
from subject.models import subject

# Create your models here.
class hr(models.Model):
    hrid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    bpm = models.DecimalField(max_digits=10, decimal_places=2) 
    time = models.DecimalField(max_digits=10, decimal_places=2) 