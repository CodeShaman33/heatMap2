import pandas as pd
import numpy as np
import glob
import folium
from folium.plugins import HeatMap
import json
import random
from sklearn.neighbors import NearestNeighbors

# List all the CSV files in the folder
csv_files = glob.glob('/*.csv')

# Define the Europe boundaries
europe_boundaries = {
    'min_lat': 49.0,
    'max_lat': 55.0,
    'min_lon': 14.0,
    'max_lon': 24.0
}

# Define the number of hexagons for the grid
num_hexagons_x = 23
num_hexagons_y = 23

# Calculate the step size for each hexagon
step_size_lat = (europe_boundaries['max_lat'] - europe_boundaries['min_lat']) / num_hexagons_y
step_size_lon = (europe_boundaries['max_lon'] - europe_boundaries['min_lon']) / num_hexagons_x

# Create an empty list to store the hexagon coordinates and signal quality values
hexagon_coords = []
signal_quality = []

# Generate random signal quality values for each hexagon
for i in range(num_hexagons_x):
    for j in range(num_hexagons_y):
        center_lat = europe_boundaries['min_lat'] + (j + 0.5) * step_size_lat
        center_lon = europe_boundaries['min_lon'] + (i + 0.5) * step_size_lon
        hexagon_coords.append((center_lat, center_lon))
        signal_quality.append(random.randint(0, 10))

# Generate a grid of points to interpolate the signal quality values
grid_x, grid_y = np.mgrid[europe_boundaries['min_lat']:europe_boundaries['max_lat']:100j,
                          europe_boundaries['min_lon']:europe_boundaries['max_lon']:100j]

# Interpolate the signal quality values over the grid
grid_points = np.array(hexagon_coords)
grid_values = np.array(signal_quality)
neigh = NearestNeighbors(n_neighbors=4)
neigh.fit(grid_points)
distances, indices = neigh.kneighbors(np.c_[grid_x.ravel(), grid_y.ravel()])
grid_z = np.mean(grid_values[indices], axis=1)

# Create a folium map centered around Europe
map_center = [(europe_boundaries['min_lat'] + europe_boundaries['max_lat']) / 2,
              (europe_boundaries['min_lon'] + europe_boundaries['max_lon']) / 2]
map_zoom = 6
folium_map = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True)

# Create a HeatMap layer with the interpolated signal quality values
HeatMap(zip(grid_x.flatten(), grid_y.flatten(), grid_z.flatten()), gradient={0.0: 'red', 1.0: 'green'}).add_to(folium_map)

# Save the folium map as an HTML file
folium_map.save('heatmap.html')
