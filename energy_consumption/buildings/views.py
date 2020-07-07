import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from django.http import JsonResponse
from .models import Building, Meter, Fuel, Readings


def meter_chart(request, meter_id):
    labels = []
    data = []
    meter = Meter.objects.get(pk=meter_id)
    readingset = meter.readings_set.all()
    for reading in readingset:
        labels.append(reading.reading_data_time)
        data.append(reading.consumption)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def index(request):
  buildings = Building.objects.order_by()
  context = {'buildings': buildings}
  return render(request, 'buildings/index.html', context)

def meter_detail(request, building_id):
  building = Building.objects.get(pk=building_id)
  return render(request, 'buildings/meter_detail.html', { 'building': building })

def meter_readings(request, meter_id):
  meter = Meter.objects.get(pk=meter_id)
  return render(request, 'buildings/meter_readings.html', { 'meter': meter })

def building_upload(request):    
  # View to upload a csv of buildings
  template = "building_upload.html"
  data = Building.objects.all()
  prompt = {
      'order': 'Order of the CSV should be id, name',
      'buildings': data    
            }

  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    
  
  # Check for csv file
  if not csv_file.name.endswith('.csv'):
      messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')

  # Stream to loop through each line in the data
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    if not column[0] or column[1]:
      continue 
    _, created = Building.objects.update_or_create(
          id=column[0],
          name=column[1],
      )
  context = {}
  return render(request, template, context)


def meter_upload(request):    
  # View to upload a csv of buildings
  template = "meter_upload.html"
  data = Meter.objects.all()
  prompt = {
      'order': 'Order of the CSV should be building_id, id, fuel, unit',
      'meters': data    
            }

  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    
  
  # Check for csv file
  if not csv_file.name.endswith('.csv'):
      messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')
  
  # Stream to loop through each line in the data
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    if not column[0] or not column[1] or not column[2] or not column[3]:
      continue 

    _, created_fuel = Fuel.objects.update_or_create(
      fuel=column[2],
      unit=column[3]
    )
    _, created_meter = Meter.objects.update_or_create(
          building=Building.objects.get(pk=column[0]),
          id=column[1],
          fuel=Fuel.objects.get(pk=column[2]),
      )

  context = {}
  return render(request, template, context)


def reading_upload(request):    
  # View to upload a csv of buildings
  template = "meter_upload.html"
  data = Meter.objects.all()
  prompt = {
      'order': 'Order of the CSV should be consumption, meter id, reading date-time',
      'readings': data    
            }

  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    
  
  # Check for csv file
  if not csv_file.name.endswith('.csv'):
      messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')
  
  # Stream to loop through each line in the data
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    if not column[0] or not column[1] or not column[2]:
      continue 

    _, created_reading = Readings.objects.update_or_create(
      meter_id=Meter.objects.get(pk=column[1]),
      consumption=column[0],
      reading_data_time=column[2]
    )

  context = {}
  return render(request, template, context)