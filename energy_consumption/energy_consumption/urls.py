"""energy_consumption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from buildings.views import building_upload, meter_upload, reading_upload, meter_detail
urlpatterns = [
    url(r'^', include('pages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^buildings/', include('buildings.urls')),
    url(r'^upload-building/', building_upload, name="building_upload"),
    url(r'^upload-meter/', meter_upload, name="meter_upload"),
    url(r'^upload-readings/', reading_upload, name="reading_upload"),
]
