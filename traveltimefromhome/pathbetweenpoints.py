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


# Helper functions
def get_file_contents(filename):
    """ Given a filename, return the contents of that file"""
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


def convert_coord(coordinates):
    """
    Convert coordinates from [lon, lat] to [lat, lon] format
    Needed for the folium map since the order is different compared to
    Graphhopper
    """
    coordinates1 = [None, None]
    coordinates1[0] = coordinates[1]
    coordinates1[1] = coordinates[0]
    return coordinates1


# Settings
filename = 'apikey'
coords = [[13.413706, 52.490202],
          [13.421838, 52.514105],
          [13.453649, 52.507987],
          [13.401947, 52.543373]]
profile = 'car'


def main():

    # Get API key
    api_key = get_file_contents(filename)

    # Initialize Graphhopper client
    client = Graphhopper(api_key=api_key)

    # Get route from Graphhopper
    route = client.directions(locations=coords, profile=profile)

    # Create map
    start_location = convert_coord(coords[0])
    m = folium.Map(location=start_location, zoom_start=11)

    # Add markers for coordinates
    for coord in coords:
        folium.Marker(
            location=convert_coord(coord),
            tooltip="Click me!",
            icon=folium.Icon(color="green"),
        ).add_to(m)

    # Add route polyline
    geometry = [convert_coord(coord) for coord in route.geometry]
    folium.PolyLine(geometry, tooltip="Route").add_to(m)

    # Save map
    m.save("index.html")


if __name__ == "__main__":
    main()
