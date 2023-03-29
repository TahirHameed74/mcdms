from django.contrib import admin
from . models import carParameters
from . models import houseParameters

# Register your models here.

admin.site.register(carParameters)
admin.site.register(houseParameters)