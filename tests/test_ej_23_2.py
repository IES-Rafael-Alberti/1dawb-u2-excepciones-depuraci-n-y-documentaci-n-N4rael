import pytest
from src.ej_23_2 import bucle

@pytest.mark.parametrize(
    "input, expected",
    [
        (2, '1'),
        (1, '1'),
        (10, '1, 3, 5, 7, 9'),
        (17, '1, 3, 5, 7, 9, 11, 13, 15, 17'),
        (18, '1, 3, 5, 7, 9, 11, 13, 15, 17'),
        (100, '1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99')
    ]
)

def testBucle(input, expected):
    assert bucle(input) == expected