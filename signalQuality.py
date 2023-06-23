import folium

def generate_europe_map():
    # Create a Europe map centered on a specific location
    europe_map = folium.Map(location=[54.5260, 15.2551], zoom_start=4)

    # Add markers for main cities
    cities = {
        'London': [51.5074, -0.1278],
        'Paris': [48.8566, 2.3522],
        'Berlin': [52.5200, 13.4050],
        'Madrid': [40.4168, -3.7038],
        'Rome': [41.9028, 12.4964],
        'Athens': [37.9838, 23.7275],
        'Stockholm': [59.3293, 18.0686],
        'Moscow': [55.7558, 37.6176],
        'Lisbon': [38.7223, -9.1393],
        'Dublin': [53.3498, -6.2603]
    }

    for city, coordinates in cities.items():
        folium.Marker(location=coordinates, popup=city).add_to(europe_map)

    # Display the map
    return europe_map

# Generate and display the Europe map
generate_europe_map()