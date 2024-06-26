"""
util.py

This module contains helper functions for the pathbetweenpoints script.
"""

# Helper functions


def get_file_contents(filename):
    """ Given a filename, return the contents of that file"""
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


def convert_coordinates(coordinates):
    """
    Convert coordinates from [lon, lat] to [lat, lon] format
    Needed for the folium map since the order is different compared to
    Graphhopper
    """
    coordinates1 = [None, None]
    coordinates1[0] = coordinates[1]
    coordinates1[1] = coordinates[0]
    return coordinates1


def split_coordinates(coordinates):
    """
    Transform the list of dictionaries into a list of lists
    """
    coordinates_list = [[coord["longitude"], coord["latitude"]]
                        for coord in coordinates]
    cityname_list = [coord["city"]
                     for coord in coordinates]
    return coordinates_list, cityname_list
