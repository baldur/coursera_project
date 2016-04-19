import pandas as pd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from shapely.geometry import Point
data_blight = pd.read_csv('./detroit-blight-violations.csv')

data_blight['coordinates'] = data_blight['ViolationAddress'].apply(lambda x: x.split('\n')[-1].replace('(','').replace(')',''))

data_blight['lat'] = data_blight['coordinates'].apply(lambda x: x.split(', ')[0])
data_blight['lng'] = data_blight['coordinates'].apply(lambda x: x.split(', ')[1])

data_blight['lat'] = data_blight.lat.astype(float)
data_blight['lng'] = data_blight.lng.astype(float)
data_blight['building_street_address'] = data_blight['ViolationAddress'].apply(lambda x: x.split('\n')[0])

unique_buildings = data_blight.loc[:,['building_street_address', 'lat', 'lng']].drop_duplicates()

#unique_buildings.to_csv('unique_blight_buildings.csv')

data_311 = pd.read_csv('./detroit-311.csv')
data_311['building_street_address'] = data_311['address'].apply(lambda x: x.split(',')[0].replace(' Detroit', ''))
unique_buildings_311 = data_311.loc[:,['building_street_address', 'lat', 'lng']].drop_duplicates()


data_crime = pd.read_csv('./detroit-crime.csv')
data_crime['lat'] = data_crime['LAT']
data_crime['lng'] = data_crime['LON']
data_crime['building_street_address'] = data_crime['ADDRESS']
unique_buildings_crime = data_crime.loc[:,['building_street_address', 'lat', 'lng']].drop_duplicates()


combined = pd.concat([unique_buildings, unique_buildings_311, unique_buildings_crime])

#geometry = [Point(xy) for xy in zip(data.lng, data.lat)]
#crs=None
#geo_df = GeoDataFrame(data, crs=crs, geometry=geometry)



