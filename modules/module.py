#Imports
import pandas as pd
import requests
import argparse


file_path = '../data/bicimad_stations.csv'
url = 'https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json'


#1.Acquisition & Wrangling
## Acquisition

def acquisition_method_csv(file_path):
    df_acquisition_csv = pd.read_csv(file_path, sep="\t")
    return df_acquisition_csv

def acquisition_method_api(url):
    response = requests.get(url)
    json_data = response.json()
    df_acquisition_api = pd.DataFrame(json_data['@graph'])
    return df_acquisition_api

## Clean DF

def clean_df_stations(df_acquisition_csv):
    df_acquisition_csv[['longitud', 'latitud']] = df_acquisition_csv['geometry.coordinates']\
    .str.strip('[]').str.split(', ', expand=True).astype(float)
    df_acquisition_csv['name'] = df_acquisition_csv['name'].str.extract(r'\s-\s(.*)')
    df_bicimad_stations = df_acquisition_csv[['name', 'address', 'latitud', 'longitud', 'dock_bikes']].rename(columns={
        'name': 'BiciMAD station', 
        'address': 'Station location', 
        'latitud': 'station_lat',
        'longitud': 'station_long',
        'dock_bikes': 'Bikes_available' 
    })
    return df_bicimad_stations

def clean_df_places(df_acquisition_api):
    df_acquisition_api['street_address'] =  df_acquisition_api['address']\
    .apply(lambda x: x.get('street-address') if pd.notnull(x) else None).str.title()
    
    df_acquisition_api['latitude'] =  df_acquisition_api['location']\
    .apply(lambda x: x['latitude'] if isinstance(x, dict) else None)
    df_acquisition_api['longitude'] =  df_acquisition_api['location']\
    .apply(lambda x: x['longitude'] if isinstance(x, dict) else None)
    
    df_places =  df_acquisition_api[['title', 'street_address', 'latitude', 'longitude']].rename(columns={
        'title': 'Place of interest', 
        'street_address': 'Place address', 
        'latitude': 'place_lat', 
        'longitude': 'place_long'
    })
    df_places = df_places.dropna().reset_index(drop=True)
    return df_places

## Build DF 

def combine_dataframes_cross (df1, df2):
    df_combined = pd.merge(df1, df2, how = 'cross').copy()
    return df_combined

#2.Analysis

#Calculate distance

def calculate_distance_pitagoras(lat1, lon1, lat2, lon2):
    distance = ((lat2 - lat1)**2 + (lon2 - lon1)**2)**0.5
    return distance


def find_nearest_stations (df_combined):
    df_combined['distance'] = df_combined.apply(lambda row: calculate_distance_pitagoras(
        row['station_lat'], row['station_long'], row['place_lat'], row['place_long']),axis=1)
    nearest_stations = df_combined.loc[df_combined.groupby('Place of interest')['distance'].idxmin()]
    final_result = nearest_stations[['Place of interest', 'Place address', 'BiciMAD station', 'Station location', 'Bikes_available']]
    return final_result

#3.Save result

def save_to_csv (dataframe):
    dataframe.to_csv('./data/nearest_bicimad_stations.csv')
    print ("---Your file has been saved as ./data/nearest_bicimad_stations.csv---")

#4.Choose posibility:

def argument_parser():
    parser = argparse.ArgumentParser(description="Get stations near points of interest.")
    help_message ='You have two options. 1. "all": Get table with information for all places. 2. "place": obtain a table corresponding to a specific place provided by the user.'
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args

