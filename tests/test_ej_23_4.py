import pytest
from src.ej_23_4 import pedirNumero

@pytest.mark.parametrize(
    "input, expected",
    [
        ("18", "Correcto"),
        ("18.5", "La entrada no es correcta"),
        ("hola", "La entrada no es correcta"),
        ("7", "Correcto"),
        ("+", "La entrada no es correcta")
    ]
)

def testNumer(input, expected):
    assert pedirNumero(input) == expected