# 🚲 **BiciMAD Stations & Points of Interest Near You** 

Welcome to the **BiciMAD Stations & Points of Interest** application! 🚴‍♂️ This project aims to help users locate the nearest BiciMAD bike stations to **educational centers** across Madrid. It is developed as part of the final project for **Module 1** of the **Ironhack Data Analytics Bootcamp**. 🎓

---

## 📚 Table of Contents
- [💾 Data](#💾-data)
- [⏩ How it works](#⏩-how-it-works)
- [💻 Technology Stack](#💻-technology-stack)
- [⚙️ Installation](#⚙️-installation)
- [📁 Folder Structure](#📁-folder-structure)
---

## 💾 Data:

The project uses **2 main datasets**:

1. **BiciMAD Stations**: 
   - This dataset provides information about **BiciMAD bike stations** in Madrid.
   - You can find this dataset in the file: `bicimad_stations.csv`.

2. **Educational Centers**:
   - This dataset contains information about **educational centers** in Madrid. The application fetches this data from a public API.
   - Data source: [Madrid Educational Centers API](https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json).

---

## ⏩ How it works

The application fetches data from two sources: a local CSV file with **BiciMAD stations** and a public API for **educational centers** in Madrid. Here's how it works:

1. **Data Acquisition**: 
   - **BiciMAD Stations** data is loaded from the CSV file `bicimad_stations.csv`.  
   - **Educational Centers** data is fetched via the Madrid open data API.

2. **Data Cleaning**: 
   - Clean the BiciMAD stations dataset to extract station name, address, latitude, longitude, and available bikes.  
   - Clean the educational centers dataset to extract names, addresses, and geolocations.

3. **Data Combination**: 
   - A **cross join** is performed to combine each BiciMAD station with every educational center, so that distances can be calculated.

4. **Distance Calculation**: 
   - The application calculates the distance between each educational center and its nearest BiciMAD station using the **Pythagorean theorem**.

5. **Results**: 
   - The nearest BiciMAD station for each educational center is identified and saved into a CSV file (`nearest_bicimad_stations.csv` or `nearest_bicimad_stations_all.csv`).

---

## 💻 Technology Stack

This project uses the following libraries and versions:

- **pandas**: `pandas==2.1.4`
- **requests**: `requests==2.31.0`

---

## ⚙️ Installation

1. **Clone the repository**  
   To get the project on your local machine, clone the repository with the following command:
   ```bash
   git clone https://github.com/yourusername/bicimad-project.git
   ```
2. **Install dependencies**  
   Install the required dependencies listed in the `requirements.txt` file using:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**  
   To execute the script and generate the results, use the following commands depending on the option you want:
   
   - **To obtain a table with all the information (all places of interest)**  
   ```bash
   python main.py -f all
   ```
   This will process all available places of interest and generate a CSV file with the nearest BiciMAD stations for each place. The result will be saved as nearest_bicimad_stations_all.csv in the ./data/ folder.

   - **To obtain a table corresponding to a specific place provided by the user**  
   ```bash
   python main.py -f place
   ```

   This option will process a specific place of interest and generate a CSV file with the nearest BiciMAD station for that place. After running the command, you will be prompted to enter the name of the place.After running the command, you will be asked to enter the name of the place and the result will be saved as nearest_bicimad_station.csv in the ./data/ folder. 
---

## 📁 Folder Structure

The project folder structure is as follows:
```text
└── Project
    ├── .gitignore
    ├── README.md
    ├── main.py
    ├── notebooks
    │   ├── BiciMad_Station_DF.ipynb
    │   ├── Final_DF.ipynb
    │   └── Places_DF.ipynb
    ├── modules
    │   └── module.py
    └── data
        ├── bicimad_stations.csv
        ├── bicipark_stations.csv
        ├── nearest_bicimad_station.csv    
        └── nearest_bicimad_stations_all.csv
```