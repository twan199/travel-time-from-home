"""
test_pathbetweenpoints.py

This module contains unit tests for the pathbetweenpoints script.
"""

from traveltimefromhome.util import convert_coordinates


def test_convert_coordinates():
    # Test case for converting coordinates
    assert convert_coordinates([13.413706, 52.490202]) == [
        52.490202, 13.413706]
