import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(10, -5) == 15

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-4, 5) == -20

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(8, 4) == 2

    with pytest.raises(ValueError):
        dividir(10, 0)
