"""
pathbetweenpoints.py

This script uses the Graphhopper API and the folium library to plot a route
between multiple coordinates on a map. It takes a list of coordinates, fetches
the route from the Graphhopper API, and generates an HTML file with a map
displaying the route and markers for the given coordinates.

Needs a file apikey which contains the api key for the Graphhopper API.
"""

import folium
from routingpy import Graphhopper
from util import get_file_contents, convert_coordinates, split_coordinates

# Settings
filename = 'apikey'
coordinates = [
    {"city": "Assen", "latitude": 53.0047, "longitude": 6.5622},
    {"city": "Leeuwarden", "latitude": 53.2012, "longitude": 5.7999},
    {"city": "Groningen", "latitude": 53.2194, "longitude": 6.5665},
    {"city": "Arnhem", "latitude": 51.9851, "longitude": 5.8987}]
profile = 'car'


def main():

    # Get API key
    api_key = get_file_contents(filename)

    # Initialize Graphhopper client
    client = Graphhopper(api_key=api_key)

    # Transform the list of dictionaries into a list of lists
    coordinates_list, cityname_list = split_coordinates(coordinates)

    # Get route from Graphhopper
    route = client.directions(locations=coordinates_list, profile=profile)

    # Create map
    start_location = convert_coordinates(coordinates_list[0])
    m = folium.Map(location=start_location, zoom_start=11)

    # Add markers for coordinates
    for i in range(len(coordinates_list)):
        folium.Marker(
            location=convert_coordinates(coordinates_list[i]),
            tooltip=cityname_list[i],
            icon=folium.Icon(color="green"),
        ).add_to(m)

    # Add route polyline
    geometry = [convert_coordinates(coord) for coord in route.geometry]
    folium.PolyLine(geometry, tooltip="Route").add_to(m)

    # Save map
    m.save("index.html")


if __name__ == "__main__":
    main()
