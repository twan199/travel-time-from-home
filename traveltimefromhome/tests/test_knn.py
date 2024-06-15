"""
test_knn.py

This module contains unit tests for the knn.py script.
"""

from model.knn import euclidean_distance2d, knn
import pytest


test_coordinates = [
    {"city": "CityA", "latitude": 1.0, "longitude": 2.0},
    {"city": "CityB", "latitude": 3.0, "longitude": 4.0},
    {"city": "CityC", "latitude": 5.0, "longitude": 6.0},
    {"city": "CityD", "latitude": 7.0, "longitude": 8.0},
    {"city": "CityE", "latitude": 9.0, "longitude": 10.0},
    {"city": "CityF", "latitude": 11.0, "longitude": 12.0},
    {"city": "CityG", "latitude": 13.0, "longitude": 14.0},
    {"city": "CityH", "latitude": 15.0, "longitude": 16.0},
    {"city": "CityI", "latitude": 17.0, "longitude": 18.0},
    {"city": "CityJ", "latitude": 19.0, "longitude": 20.0},
    {"city": "CityK", "latitude": 21.0, "longitude": 22.0},
    {"city": "CityL", "latitude": 23.0, "longitude": 24.0},
    {"city": "CityM", "latitude": 25.0, "longitude": 26.0}
]


def test_knn():
    # Test case 1: Starting from CityA
    start_city = "CityA"
    expected_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]
    assert knn(test_coordinates, start_city) == expected_order

    # Test case 2: Starting from CityM
    start_city = "CityM"
    expected_order = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12]
    assert knn(test_coordinates, start_city) == expected_order

    # Test case 3: Different city names
    different_names = [{"city": f"City{i}", "latitude": coord["latitude"],
                        "longitude": coord["longitude"]}
                       for i, coord in enumerate(test_coordinates)]
    start_city = "City0"
    expected_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]
    assert knn(different_names, start_city) == expected_order

    # Test case 4: Negative coordinates
    negative_coordinates = [{"city": coord["city"],
                             "latitude": -coord["latitude"],
                             "longitude": -coord["longitude"]}
                            for coord in test_coordinates]
    start_city = "CityA"
    expected_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]
    assert knn(negative_coordinates, start_city) == expected_order

    # Test case 5: Duplicate coordinates
    duplicate_coordinates = test_coordinates + test_coordinates[1:5]
    start_city = "CityA"
    expected_order = [0, 1, 13, 2, 14, 3, 15, 4,
                      16, 5, 6, 7, 8, 9, 10, 11, 12, 0]
    assert knn(duplicate_coordinates, start_city) == expected_order


def test_euclidean_distance2d():
    # Test case 1: Simple example
    coord1 = (0, 0)
    coord2 = (3, 4)
    expected_distance = 5.0
    assert euclidean_distance2d(
        coord1, coord2) == pytest.approx(expected_distance)

    # Test case 2: Negative coordinates
    coord1 = (-2, -3)
    coord2 = (4, 5)
    expected_distance = 10.0
    assert euclidean_distance2d(
        coord1, coord2) == pytest.approx(expected_distance)

    # Test case 3: Same coordinates
    coord1 = (1, 1)
    coord2 = (1, 1)
    expected_distance = 0.0
    assert euclidean_distance2d(
        coord1, coord2) == pytest.approx(expected_distance)
