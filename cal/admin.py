from django.contrib import admin
from cal.models import Event,DelEvent,Email

# Register your models here.
admin.site.register(Event)
admin.site.register(Email)
admin.site.register(DelEvent)