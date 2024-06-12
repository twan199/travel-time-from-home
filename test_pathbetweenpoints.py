import pytest
from pathbetweenpoints import convert_coord


def test_convert_coord():
    # Test case for converting coordinates
    coords = [13.413706, 52.490202]
    expected_result = [52.490202, 13.413706]
    result = convert_coord(coords)
    assert result == expected_result
