#imports

from modules import module as md

#input

file_path = './data/bicimad_stations.csv'
url = 'https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json'

#pipeline

if __name__ == '__main__':

    args = md.argument_parser()

    df_acquisition_csv = md.acquisition_method_csv(file_path)
    df_acquisition_api = md.acquisition_method_api(url)
    df_bicimad_stations = md.clean_df_stations(df_acquisition_csv)
    df_places = md.clean_df_places(df_acquisition_api)
    df_combined = md.combine_dataframes_cross(df_bicimad_stations, df_places)

    if args.function == 'all':
        final_results = md.find_nearest_stations(df_combined)
        final_results.to_csv('./data/nearest_bicimad_stations_all.csv', index=False)
        print("---Your file has been saved as ./data/nearest_bicimad_stations_all.csv---")
        

    elif args.function == 'place':
        place_name = input("Enter the name of the Place of Interest: ").strip()
        filtered_df = df_combined[df_combined['Place of interest'] == place_name]
        final_results = md.find_nearest_stations(filtered_df)
        final_results.to_csv('./data/nearest_bicimad_stations.csv', index=False)
        print("---Your file has been saved as ./data/nearest_bicimad_station.csv---")
        print(final_results) 

    else:
        print("You must provide at least one valid option (use --help for help).")
        exit()

    
    
