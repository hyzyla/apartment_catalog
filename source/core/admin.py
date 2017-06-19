from django.contrib import admin

# Register your models here.

from .models import (Project, Apartment, 
	BoodCompany, District, Picture)

admin.site.register(Project)
admin.site.register(Apartment)
admin.site.register(BoodCompany)
admin.site.register(District)
admin.site.register(Picture)