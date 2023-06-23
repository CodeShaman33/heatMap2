import pandas as pd
import folium
from folium import Choropleth
import geopandas as gpd
from shapely.geometry import Polygon


# Define the Europe boundaries
# For now, there are Poland boundaries
europe_boundaries = {
    'min_lat': 49.0,
    'max_lat': 55.0,
    'min_lon': 14.0,
    'max_lon': 24.0
}


min_lat = 49.0
max_lat = 55.0
min_lon = 14.0
max_lon = 24.0

polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat), (min_lon, max_lat)])


gdf = gpd.GeoDataFrame({'geometry': [polygon]})


gdf.to_file('poland.geojson', driver='GeoJSON')


# Read the GeoJSON file
poland_geojson = 'poland.geojson'
poland_data = gpd.read_file(poland_geojson)

# Create the Choropleth map


# Define the number of hexagons for the grid
num_hexagons_x = 1111
num_hexagons_y = 1111

# Variable for maximum value
max_value = 0

# Calculate the step size for each hexagon
step_size_lat = (europe_boundaries['max_lat'] - europe_boundaries['min_lat']) / num_hexagons_y
step_size_lon = (europe_boundaries['max_lon'] - europe_boundaries['min_lon']) / num_hexagons_x

# Create a table, where rows and columns are based on hexagon number
grid = [[[] for _ in range(num_hexagons_y)] for _ in range(num_hexagons_x)]

# Calculate step size, each hexagon has a corresponding cell in the table
# which is another table that contains coordinates as a tuple and
# another variable which is the sum of every reading
for i in range(num_hexagons_x):
    for j in range(num_hexagons_y):
        center_lat = europe_boundaries['min_lat'] + (i + 0.5) * step_size_lat
        center_lon = europe_boundaries['min_lon'] + (j + 0.5) * step_size_lon
        grid[i][j].append((center_lat, center_lon))
        grid[i][j].append(0)
        grid[i][j].append(0)

# Iterate over each CSV file
csv_file = 'position examples\patryk.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file, header=None, delimiter=';', encoding='utf-8', skiprows=1)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    try:
        # Signal quality extracted from the CSV file
        data = row[5].split(',')
        lastPart = data[4][:3]
        signalQuality = float(row[4][3:5])

        # Position
        lat = float(data[0] + '.' + data[1])
        lon = float(data[3] + '.' + lastPart)

        # Check if the GPS coordinates are within the Europe boundaries
        if (
            europe_boundaries['min_lat'] <= lat <= europe_boundaries['max_lat'] and
            europe_boundaries['min_lon'] <= lon <= europe_boundaries['max_lon']
        ):
            # Calculate the grid indices for the current GPS coordinates
            lat_index = int((lat - europe_boundaries['min_lat'] - 0.25 * step_size_lat) // step_size_lat)
            lon_index = int((lon - europe_boundaries['min_lon'] - 0.25 * step_size_lon) // step_size_lon)

            # Increment the signal quality value in the corresponding grid cell
            grid[lat_index][lon_index][1] += signalQuality
            grid[lat_index][lon_index][2] += 1

    except:
        continue

# Create a folium map centered around Europe
map_center = [(europe_boundaries['min_lat'] + europe_boundaries['max_lat']) / 2,
              (europe_boundaries['min_lon'] + europe_boundaries['max_lon']) / 2]
map_zoom = 6
folium_map = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True, tiles='cartodbpositron')

# Creating final dictionary for choropleth data
choropleth_data = {}

for row in grid:
    for table in row:
        coordinate, value, iterations = table
        if iterations == 0:
            finalValue = 0
        else:
            finalValue = value / iterations

            # Creating maximum value
            if finalValue > max_value:
                max_value = finalValue

        choropleth_data[str(coordinate)] = finalValue
        
choropleth_data = {
    "region1": 10,  # Signal quality value for region1
    "region2": 20,  # Signal quality value for region2
    "region3": 5,   # Signal quality value for region3
    # Add more regions and their corresponding signal quality values
}

# Create a Choropleth map using the hexagonal grid data
Choropleth(
    geo_data=poland_data,  # Provide your own GeoJSON data if available
    data=choropleth_data,
    key_on='feature.properties.region_id',  # Update with the correct feature ID property from your GeoJSON data
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Signal Quality',
).add_to(folium_map)

# Save the folium map as an HTML file
folium_map.save('choropleth.html')
