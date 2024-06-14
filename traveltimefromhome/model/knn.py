"""
K-Nearest Neighbors algorithm

knn.py
"""
import numpy as np
from model.util import split_coordinates
# from sklearn.neighbors import NearestNeighbors


def euclidean_distance2d(coord1, coord2):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


def knn(coordinates, start_city):
    """
    Implement the K-Nearest Neighbors algorithm.
    Returns a list of indices representing the order of coordinates
    from the closest to the farthest from the start_city.

    Args:
        coordinates (list): A list of coordinates [x, y].
        start_city (str): The name of the starting city.

    Returns:
        list: A list of indices representing the order of coordinates
              from the closest to the farthest from the start_city.
    """
    coordinates_list, cityname_list = split_coordinates(coordinates)

    # Find the index of the start_city in the cityname_list
    start_idx = cityname_list.index(start_city)

    # Initialize the index_list_order with the starting index
    index_list_order = [start_idx]
    start_coordinate = coordinates_list[start_idx]

    for i in range(len(coordinates_list)-1):

        # Calculate the Euclidean distance between the current point and the
        # start point
        distances = [euclidean_distance2d(start_coordinate, coordinate)
                     for coordinate in coordinates_list]

        # Find the index of the coordinate with the minimum distance that
        # hasn't been added to index_list_order yet
        minimum_idx = min((i for i, d in enumerate(
            distances) if i not in index_list_order),
            key=lambda i: distances[i])

        # Append the minimum distance index to index_list_order
        index_list_order.append(minimum_idx)

        # Update the start_coordinate to the coordinate at the minimum index
        start_coordinate = coordinates_list[minimum_idx]

    # Append the starting index to index_list_order again since it is a round
    # trip
    index_list_order.append(start_idx)
    return index_list_order
