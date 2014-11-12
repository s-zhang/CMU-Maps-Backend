from django.contrib.gis import admin
from models import Room, Floor, Building

admin.site.register(Room, admin.OSMGeoAdmin)
admin.site.register(Floor, admin.OSMGeoAdmin)
admin.site.register(Building, admin.OSMGeoAdmin)