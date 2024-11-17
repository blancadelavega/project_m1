# 🚲 **BiciMAD Stations & Points of Interest Near You** 

Welcome to the **BiciMAD Stations & Points of Interest** application! 🚴‍♂️ This project aims to help users locate the nearest BiciMAD bike stations to **educational centers** across Madrid. It is developed as part of the final project for **Module 1** of the **Ironhack Data Analytics Bootcamp**. 🎓


## 💾 Data:
There are 2 different datasource involved:

1. **BiciMAD Stations**: 
   - This is the primary dataset used to get information about the **BiciMAD bike stations** in Madrid. 
   - You can find this dataset in the file: `bicimad_stations.csv`.

2. **Educational Centers**:
   - This dataset provides data about the **educational centers** in Madrid. The application fetches this data from a public API.
   - This data is obtained from the API located at: `https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json`.


## ⏩ How it works

The application fetches data from two main sources: a local CSV file containing **BiciMAD bike stations** and a public API providing information about **educational centers** in Madrid. The process involves several steps:

1. **Data Acquisition**: 
   - The data about BiciMAD stations is loaded from a CSV file (`bicimad_stations.csv`).
   - The data about educational centers is fetched from the Madrid open data API.
   
2. **Data Cleaning**: 
   - The dataset for BiciMAD stations is cleaned to extract relevant details such as station name, address, latitude, longitude, and available bikes.
   - The educational centers dataset is cleaned to extract the name, address, and geolocation of each center.
   
3. **Data Combination**: 
   - A **cross join** is performed to combine each BiciMAD station with every educational center, so that distances can be calculated.

4. **Distance Calculation**: 
   - The application calculates the distance between each educational center and its nearest BiciMAD station using the **Pythagorean theorem**.

5. **Results**: 
   - The nearest BiciMAD station for each educational center is identified and saved into a CSV file (`nearest_bicimad_stations.csv` or `nearest_bicimad_stations_all.csv`).

To run the script and get the results, simply execute the following command in your terminal:

```bash
python main.py

 **💻 Technology stack **
pandas==2.1.4
requests==2.31.0


 **📁 Folder Structure**

The project folder structure is as follows:
```text
└── Project
    ├── .gitignore
    ├── README.md
    ├── main.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   ├── notebook2.ipynb
    │   └── notebook3.ipynb
    ├── modules
    │   └── module.py
    └── data
        ├── bicimad_stations.csv
        ├── bicipark_stations.csv
        ├── nearest_bicimad_station.csv    
        └── nearest_bicimad_stations_all.csv


