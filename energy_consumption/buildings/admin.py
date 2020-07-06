from django.contrib import admin

from .models import Building, Meter

class MeterInline(admin.TabularInline):
  model = Meter

class BuildingAdmin(admin.ModelAdmin):
  model = Building
  inlines = [MeterInline]

admin.site.register(Building, BuildingAdmin)