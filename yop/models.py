from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from datetime import datetime
class Event(models.Model):
    program = models.CharField(max_length=250)
    spot = models.CharField(max_length=250)
    start_date = models.CharField(max_length=250)
    start_time = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    uid = models.IntegerField()

now = datetime.utcnow()
class EventAdmin(admin.ModelAdmin):
    list_display = ['program', 'spot', 'start_time', 'duration', 'description', 'uid']
admin.site.register(Event, EventAdmin)