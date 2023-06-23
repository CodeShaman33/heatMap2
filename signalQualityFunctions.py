import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon
import glob


# List all the CSV files in the folder
csv_files = glob.glob('CSV files/*.csv')



# Define the Europe boundaries
europe_boundaries = {
    'min_lat': 36.0,
    'max_lat': 72.0,
    'min_lon': -11.0,
    'max_lon': 45.0
}


# Define the number of hexagons for the grid
num_hexagons_x = 1000
num_hexagons_y = 1000

# Calculate the step size for each hexagon
step_size_lat = (europe_boundaries['max_lat'] - europe_boundaries['min_lat']) / num_hexagons_y
step_size_lon = (europe_boundaries['max_lon'] - europe_boundaries['min_lon']) / num_hexagons_x

# Create an empty grid to store the signal quality values
grid = np.zeros((num_hexagons_x, num_hexagons_y))

print(grid)


for csv_file in csv_files:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, header=None, delimiter=';', encoding='utf-8', skiprows=1)
    # print(df)
    
    # for index, row in df.iterrows():
    #     if index == 100 or index == 200 or index == 300:
    #         # print(row[3])
