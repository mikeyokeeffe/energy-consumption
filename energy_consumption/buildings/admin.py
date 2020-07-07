from django.contrib import admin

from .models import Building, Meter, Readings

admin.site.site_header = "Energy Consumption"

class ReadingsInline(admin.TabularInline):
  model = Readings

class MeterInline(admin.TabularInline):
  model = Meter
  readonly_fields = ('id',)
  inlines = [Readings]

class BuildingAdmin(admin.ModelAdmin):
  model = Building
  inlines = [MeterInline]

admin.site.register(Building, BuildingAdmin)