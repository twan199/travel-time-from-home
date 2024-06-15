

import folium
from routingpy import Graphhopper
from .knn import knn
from .util import get_file_contents, convert_coordinates, split_coordinates
# Settings
filename = 'apikey'
provincial_capitals_coords = [
    {"city": "Assen", "latitude": 53.0047, "longitude": 6.5622},
    {"city": "Leeuwarden", "latitude": 53.2012, "longitude": 5.7999},
    {"city": "Groningen", "latitude": 53.2194, "longitude": 6.5665},
    {"city": "Arnhem", "latitude": 51.9851, "longitude": 5.8987},
    {"city": "Zwolle", "latitude": 52.5168, "longitude": 6.0830},
    {"city": "Lelystad", "latitude": 52.5185, "longitude": 5.4714},
    {"city": "Haarlem", "latitude": 52.3874, "longitude": 4.6462},
    {"city": "The Hague (Den Haag)", "latitude": 52.0705, "longitude": 4.3007},
    {"city": "Middelburg", "latitude": 51.4988, "longitude": 3.6103},
    {"city": "Utrecht", "latitude": 52.0907, "longitude": 5.1214},
    {"city": "'s-Hertogenbosch (Den Bosch)",
     "latitude": 51.6978, "longitude": 5.3037},
    {"city": "Maastricht", "latitude": 50.8514, "longitude": 5.6909},
    {"city": "Amsterdam", "latitude": 52.3676,
        "longitude": 4.9041}  # Not a provincial capital
]

profile = 'car'
start_city = "Amsterdam"


def main():

    # Get API key
    api_key = get_file_contents(filename)

    # Initialize Graphhopper client
    client = Graphhopper(api_key=api_key)

    index_list_order = knn(
        coordinates=provincial_capitals_coords, start_city=start_city)

    coords_incl_city = [provincial_capitals_coords[i]
                        for i in index_list_order]

    coordinates_list, cityname_list = split_coordinates(coords_incl_city)

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
