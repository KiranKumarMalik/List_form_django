from django.db import models

# Create your models here.


class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    