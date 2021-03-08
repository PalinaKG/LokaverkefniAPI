from subject.models import subject
from django.db import models


# Create your models here.
class spo2(models.Model):
    spo2id = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    oxigenation = models.DecimalField(max_digits=10, decimal_places=2) 
    time = models.DecimalField(max_digits=10, decimal_places=3)