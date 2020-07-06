from django.db import models
import re

class Building(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Fuel(models.Model):
  fuel = models.CharField(max_length=30, primary_key=True)
  unit = models.CharField(max_length=10)

  def __str__(self):
    return self.fuel

class Meter(models.Model):
  id = models.IntegerField(primary_key=True)
  building = models.ForeignKey(Building, on_delete=models.CASCADE)
  fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE) 
    
  def __str__(self):
    return self.id

class Readings(models.Model):
  class Meta:
    unique_together = (('meter_id', 'reading_data_time'),)

  meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
  reading_data_time = models.DateTimeField('Reading time')
  consumption = models.DecimalField(max_digits=20, decimal_places=4)