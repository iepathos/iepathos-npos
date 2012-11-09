from django.contrib import admin
from .models import Npo

class NpoAdmin(admin.ModelAdmin):
	fields = ('ein', 'name', 'city', 'state')
	
admin.site.register(Npo, NpoAdmin)
