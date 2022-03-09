from django.contrib import admin
from mainapp.models import Contact, Property,Interiordesign,Propertydata,Propertydetaile

# Register your models here.

admin.site.register(Contact)
admin.site.register(Property)
admin.site.register(Propertydata)
admin.site.register(Interiordesign)
admin.site.register(Propertydetaile)
