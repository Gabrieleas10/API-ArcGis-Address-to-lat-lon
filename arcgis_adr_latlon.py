from arcgis.geocoding import geocode, reverse_geocode , get_geocoders, batch_geocode
from arcgis.gis import GIS
import pandas as pd
from tqdm import tqdm

file_base = 'address.txt'
base = pd.read_csv(file_base , delimiter = ',' , encoding = 'latin9')