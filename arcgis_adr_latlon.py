from arcgis.geocoding import geocode, reverse_geocode , get_geocoders, batch_geocode
from arcgis.gis import GIS
import pandas as pd
from tqdm import tqdm

# file name
file = 'Address.csv'

# importing addresses file
adrs = pd.read_csv(file , sep =',' )

# connecting ArcGIS Server
gis = GIS()

# request function
def arcgis_req(adr):
  try:
    address = adr
    geocode_result = geocode(address , max_locations= 1 )
    lat = geocode_result[0]['attributes']['Y']
    lon = geocode_result[0]['attributes']['X']
    return pd.Series([lat , lon])
  except:
    pass
tqdm.pandas()
adrs[['Lat_GIS','Lon_GIS']] = adrs['Address'].progress_apply(arcgis_req)