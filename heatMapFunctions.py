# # Generate random signal quality values for each hexagon
# for i in range(num_hexagons_x):
#     for j in range(num_hexagons_y):
#         center_lat = europe_boundaries['min_lat'] + (j + 0.5) * step_size_lat
#         center_lon = europe_boundaries['min_lon'] + (i + 0.5) * step_size_lon
#         hexagon_coords.append((center_lat, center_lon))
#         signal_quality.append(random.randint(0, 10))



europe_boundaries = {
    'min_lat': 54.25,
    'max_lat': 54.42,
    'min_lon': 18.48,
    'max_lon': 18.72
}

#polska
europe_boundaries = {
    'min_lat': 49.0,
    'max_lat': 55.0,
    'min_lon': 14.0,
    'max_lon': 24.0
}

       lat_index = int((lat - europe_boundaries['max_lat']) // step_size_lat)
                    lon_index = int((lon - europe_boundaries['max_lon']) // step_size_lon)
                    
                    
                    lat_index = int((lat - europe_boundaries['max_lat']) // step_size_lat)
                    lon_index = int((lon - europe_boundaries['min_lon']) // step_size_lon)
                    
                    lat_index = int((europe_boundaries['max_lat'] - lat) // step_size_lat)
                    lat_index = int((europe_boundaries['max_lon'] - lon) // step_size_lat)
