from pathbetweenpoints import convert_coord


def test_convert_coord():
    # Test case for converting coordinates
    assert convert_coord([13.413706, 52.490202]) == [52.490202, 13.413706]
