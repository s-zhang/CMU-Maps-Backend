from django.contrib.gis import admin
from models import Room, Floor, Building

admin.site.register(Room, admin.GeoModelAdmin)
admin.site.register(Floor, admin.GeoModelAdmin)
admin.site.register(Building, admin.GeoModelAdmin)