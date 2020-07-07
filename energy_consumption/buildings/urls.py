from django.urls import path
from . import views

app_name = 'buildings'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:building_id>', views.meter_detail, name='meter_detail'),
  path('meter_readings/<int:meter_id>', views.meter_readings, name='meter_readings'),
]
