from django.contrib.gis.db import models

# Create your models here.

class Pointer(models.Model):
    """This is class for model of coorfinate of click on the map"""
    
    location = models.PointField()