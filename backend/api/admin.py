from django.contrib.gis import admin
from .models import Route, Jetty, Bathy, UserProfileInfo, Depth, Water_Boundary, Jetty_Bathymetry, Drivers,Boat, Ridership, Jetty_Pictures, Jetty_Videos, Jetty_Supervisors, Accident
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Route, LeafletGeoAdmin)
admin.site.register(Bathy, LeafletGeoAdmin)
admin.site.register(Jetty, LeafletGeoAdmin)
admin.site.register(UserProfileInfo)
admin.site.register(Depth, LeafletGeoAdmin)
admin.site.register(Water_Boundary, LeafletGeoAdmin)
admin.site.register(Jetty_Bathymetry)
admin.site.register(Jetty_Pictures)
admin.site.register(Jetty_Videos)
admin.site.register(Jetty_Supervisors)
admin.site.register(Drivers)
admin.site.register(Boat)
admin.site.register(Ridership)
admin.site.register(Accident)
