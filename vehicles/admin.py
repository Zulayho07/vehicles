from django.contrib import admin

from .models import Brand, Car

admin.site.register([Car, Brand])