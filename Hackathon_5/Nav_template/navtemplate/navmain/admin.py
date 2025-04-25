from django.contrib import admin
from .models import Incident

# Register your models here.

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin): # <- Customizing the admin display itself
    list_display = ('timestamp', 'name', 'location',  'incident_type')
    list_filter = ('timestamp',)
    ordering = ('timestamp',)   