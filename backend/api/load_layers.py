import os
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Route, Bathy, Jetty, Depth, DepthA, DepthB, DepthC, DepthD, Water_Boundary


#This is the layer mapping code.

"""
deptha_mapping = {
    'value': 'VALUE',
    'geom': 'MULTIPOLYGON',
}

depthb_mapping = {
    'value': 'VALUE',
    'geom': 'MULTIPOLYGON',
}

depthc_mapping = {
    'value': 'VALUE',
    'geom': 'MULTIPOLYGON',
}

depthd_mapping = {
    'value': 'VALUE',
    'geom': 'MULTIPOLYGON',
}


depth_mapping = {
    'value': 'VALUE',
    'geom': 'MULTIPOLYGON',
}


bathy_mapping = {
    'depth': 'Depth',
    'long': 'Long',
    'lat': 'Lat',
    'geom': 'MULTIPOINT',
}

route_mapping = {
    'name': 'Name',
    'route_id': 'Route_ID',
    'avg_depth': 'Avg Depth',
    'geom': 'MULTILINESTRING',
}

jetty_mapping = {
    'name': 'Name',
    'terminal': 'Terminal',
    'type': 'Type',
    'geom': 'MULTIPOINT',
}

"""

water_boundary_mapping = {
    'id_number': 'Id',
    'geom': 'MULTIPOLYGON',
}

#Adding the path to the shapefile to import
base = Path(__file__).resolve().parent.parent
"""
jetty_shp = os.path.join(base, 'templates','shapefile','jetty.shp')
route_shp = os.path.join(base, 'templates', 'shapefile','route.shp')
bathy_shp = os.path.join(base, 'templates', 'shapefile', 'bathy.shp')
depth_shp = os.path.join(base, 'templates', 'shapefile', 'depth2.shp')

deptha_shp = os.path.join(base, 'templates', 'shapefile', "spilt",'A.shp')
depthb_shp = os.path.join(base, 'templates', 'shapefile', "spilt",'B.shp')
depthc_shp = os.path.join(base, 'templates', 'shapefile', "spilt",'C.shp')
depthd_shp = os.path.join(base, 'templates', 'shapefile', "spilt",'D.shp')
"""
water_boundary_shp = os.path.join(base, 'templates', 'shapefile', 'boundary.shp')


#followed by run function to add them.
"""
def run(verbose=True):
    layer_route = LayerMapping(Route, route_shp, route_mapping, transform=False, encoding='iso-8859-1')
    layer_route.save(strict=True, verbose=verbose)

    layer_bathy = LayerMapping(Bathy, bathy_shp, bathy_mapping, transform= False, encoding='iso-8859-1')
    layer_bathy.save(strict=True, verbose=verbose)

    layer_jetty = LayerMapping(Jetty, jetty_shp, jetty_mapping, transform= False, encoding='iso-8859-1')
    layer_jetty.save(strict=True,verbose=verbose)


def run(verbose=True):
    layer_depth = LayerMapping(Depth, depth_shp, depth_mapping, transform=False, encoding='iso-8859-1')
    layer_depth.save(strict=True, verbose=verbose)


def run(verbose=True):
    layer_deptha = LayerMapping(DepthA, deptha_shp, deptha_mapping, transform=False, encoding='iso-8859-1')
    layer_deptha.save(strict=True, verbose=verbose)

    layer_depthb = LayerMapping(DepthB, depthb_shp, depthb_mapping, transform=False, encoding='iso-8859-1')
    layer_depthb.save(strict=True, verbose=verbose)

    layer_depthc = LayerMapping(DepthC, depthc_shp, depthc_mapping, transform=False, encoding='iso-8859-1')
    layer_depthc.save(strict=True, verbose=verbose)

    layer_depthd = LayerMapping(DepthD, depthd_shp, depthd_mapping, transform=False, encoding='iso-8859-1')
    layer_depthd.save(strict=True, verbose=verbose)
"""

def run(verbose=True):
    layer_boundary = LayerMapping(Water_Boundary, water_boundary_shp, water_boundary_mapping, transform=False, encoding='iso-8859-1')
    layer_boundary.save(strict=True, verbose=verbose)