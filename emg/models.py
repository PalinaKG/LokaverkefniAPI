from django.db import models
from subject.models import subject
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class emg(models.Model):
    emgid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(subject, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=15, decimal_places=8)
    f40_132 = models.DecimalField(max_digits=15, decimal_places=8)
    f132_224 = models.DecimalField(max_digits=15, decimal_places=8)
    f224_316 = models.DecimalField(max_digits=15, decimal_places=8)
    f316_408 = models.DecimalField(max_digits=15, decimal_places=8)
    f408_500 = models.DecimalField(max_digits=15, decimal_places=8)
    interval = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])
    sensor = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])