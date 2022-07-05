#Import the library
from geo.Geoserver import Geoserver

# Initialize the library
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

# Create workspace
#geo.create_workspace(workspace="laswa")

# For uploading raster data to the geoserver
#geo.create_coveragestore(layer_name='waterraster', path=r'data\raster\water_raster.tif', workspace='laswa')

# For creating postGIS connection and publish postGIS table
#geo.create_featurestore(store_name='bathy_data', workspace='laswa', db='postgres', host='127.0.0.1', pg_user='postgres',
#                        pg_password='Liferocks7071')
#geo.publish_featurestore(workspace='demo', store_name='bathy_data', pg_table='depth')


#geo.upload_style(
#    path=r"data\raster\bathy_style.sld", workspace ="laswa"
#)

geo.publish_style(
    layer_name= "waterraster", style_name= "bathy_style", workspace= "laswa"
)