import pandas as pd
import numpy as np
import glob
import folium
from folium.plugins import HeatMap
from folium.plugins import Hexbin
import tqdm


# Define the Europe boundaries
# for now there are Poland boundaries 
europe_boundaries = {
    'min_lat': 49.0,
    'max_lat': 55.0,
    'min_lon': 14.0,
    'max_lon': 24.0
}

# Define the number of hexagons for the grid
num_hexagons_x = 1111
num_hexagons_y = 1111

# Calculate the step size for each hexagon
step_size_lat = (europe_boundaries['max_lat'] - europe_boundaries['min_lat']) / num_hexagons_y
step_size_lon = (europe_boundaries['max_lon'] - europe_boundaries['min_lon']) / num_hexagons_x

# create a table, where rows and columns are based on hexagon number
grid = [[[] for _ in range(num_hexagons_y)] for _ in range(num_hexagons_x)]

# calculate step size, each hexagon has coresponding cell in table 
# which is another table, which contains coordinates as a tuple and 
# another variable which is a sum of every reading
for i in range(num_hexagons_x):
    for j in range(num_hexagons_y):
        center_lat = europe_boundaries['min_lat'] + (i + 0.5) * step_size_lat
        center_lon = europe_boundaries['min_lon'] + (j + 0.5) * step_size_lon
        grid[i][j].append((center_lat, center_lon))
        grid[i][j].append(0)
        grid[i][j].append(0)

# List all the CSV files in the folder
csv_files = glob.glob('position examples/*.csv')
filesCounter = 0


print(len(csv_files))

# Iterate over each CSV file
for csv_file in csv_files:
    #progess indicator (file in files)
    filesCounter  += 1
    indicator = filesCounter/len(csv_files)*100
    print('files progress: ', indicator)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, header=None, delimiter=';', encoding='utf-8', skiprows=1)
    
    #create variable that stores number of iteration 
    iterationNum = 0
    # num_rows = df.shape[0]
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        if (True):
            
            try:
                iterationNum += 1
                #signal quality extracteds from csv file 
                data = row[5].split(',')
                lastPart = data[4][:3]
                signalQuality = float(row[4][3:5])
                
                #position
                lat = float(data[0] + '.' + data[1])
                lon = float(data[3] + '.' + lastPart)
                
                # Check if the GPS coordinates are within the Europe boundaries
                if (europe_boundaries['min_lat'] <= lat <= europe_boundaries['max_lat'] and
                    europe_boundaries['min_lon'] <= lon <= europe_boundaries['max_lon']):
                    # # Calculate the grid indices for the current GPS coordinates
                    lat_index = int((lat - europe_boundaries['min_lat'] - 0.25 * step_size_lat) // step_size_lat)
                    lon_index = int((lon - europe_boundaries['min_lon'] - 0.25 * step_size_lon) // step_size_lon)
                    # print(lat, lon, 'index:', lat_index, lon_index, 'signal:', signalQuality, 'GRID:', grid[lat_index][lon_index])

                    # Increment the signal quality value in the corresponding grid cell
                    grid[lat_index][lon_index][1] += signalQuality
                    grid[lat_index][lon_index][2] += 1
                    iterationNum += 1
                    
      
            except:
                continue

# Create a folium map centered around Europe
map_center = [(europe_boundaries['min_lat'] + europe_boundaries['max_lat']) / 2,
              (europe_boundaries['min_lon'] + europe_boundaries['max_lon']) / 2]
map_zoom = 6
folium_map = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True)

#creating final table for calculated data
heat_data = []

maxIter = 0

with open('heat_data.txt', 'w') as heatFile:
    for row in grid:
        for table in row:
            coordinate, value, iterations = table 
            if iterations == 0:
                finalValue = 0
            else:
                finalValue = value/iterations
            heat_data.append((*coordinate, finalValue))
            if value > 0:
                heatFile.write('coordinates: ' + str(coordinate) + ' value: '+ str(value) + 'iterations: ' + 
                               str(iterations) + str(value) + 'final value: ' + str(finalValue) + '\n')
            # if maxIter < 100:
            #     print(value)
            #     maxIter += 1
            
    HeatMap(heat_data).add_to(folium_map)

    # Save the folium map as an HTML file
    folium_map.save('heatmap.html')
