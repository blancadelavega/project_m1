#imports

from modules import module as md

#input

file_path = './data/bicimad_stations.csv'
url = 'https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json'

#pipeline

if __name__ == '__main__':

    args = md.parse_arguments()

    DF_ACQUISITION_CSV = md.acquisition_method_csv(file_path)
    DF_ACQUISITION_API = md.acquisition_method_api(url)
    DF_BICIMAD_STATIONS = md.clean_df_stations(DF_ACQUISITION_CSV)
    DF_PLACES = md.clean_df_places(DF_ACQUISITION_API)
    DF_COMBINED = md.combine_dataframes_cross(DF_BICIMAD_STATIONS, DF_PLACES)

    if hasattr(args, 'specific_place_name') and args.specific_place: 
        place_name = args.specific_place_name
        DF_SPECIFIC_PLACE = DF_COMBINED[DF_COMBINED['Place of interest'].str.contains(place_name, case=False, na=False)]
        if DF_SPECIFIC_PLACE.empty:
            print(f"The place '{place_name}' is not valid or does not exist in the dataset. Please try again.")
            exit()
        FINAL_RESULTS = md.find_nearest_stations(DF_SPECIFIC_PLACE)
        print("---Your file has been saved as ./data/nearest_bicimad_station.csv---")
        FINAL_RESULTS.to_csv('./data/nearest_bicimad_stations.csv', index=False)
        print(FINAL_RESULTS) 
    elif args.all_places:  
        FINAL_RESULTS = md.find_nearest_stations(DF_COMBINED)
        print("---Your file has been saved as ./data/nearest_bicimad_stations_all.csv---")
        FINAL_RESULTS.to_csv('./data/nearest_bicimad_stations_all.csv', index=False) 
    else:
        print("You must provide at least one valid option (use --help for help).")
        exit()

    
    
