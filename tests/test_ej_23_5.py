import pytest
from src.ej_23_5 import pedir_contraseña

@pytest.mark.parametrize(
    "input, input2, expected",
    [
        ("hola_mundo", "hola_mundo", "Password is correct! Redirecting... "),
        ("hola_mundo", "hola buenas", "Incorrect Password!"),
        ("hola_mundo", "que pasa", "Incorrect Password!"),
        ("hola_mundo", "nada, todo bien", "Incorrect Password!"),
        ("hola_mundo", "me alegro, tio", "Incorrect Password!"),
        ("hola_mundo", "venga, nos vemos", "Incorrect Password!"),
        ("hola_mundo", "adiós colega", "Incorrect Password!")
    ]
)

def test_pedir_contraseña(input, input2, expected):
    assert pedir_contraseña(input, input2) == expected