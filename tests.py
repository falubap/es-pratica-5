import pytest
from calculadora import calcular

def test_adicionar():
    assert calcular('adicionar', 2, 3) == 5
    assert calcular('adicionar', -1, 1) == 0
    assert calcular('adicionar', 0, 0) == 0

def test_subtrair():
    assert calcular('subtrair', 5, 3) == 2
    assert calcular('subtrair', 0, 1) == -1
    assert calcular('subtrair', -1, -1) == 0

def test_multiplicar():
    assert calcular('multiplicar', 2, 3) == 6
    assert calcular('multiplicar', -1, 5) == -5
    assert calcular('multiplicar', 0, 10) == 0

def test_dividir():
    assert calcular('dividir', 6, 3) == 2
    assert calcular('dividir', 5, 2) == 2.5
    with pytest.raises(ValueError):
        calcular('dividir', 5, 0)

def test_calcular_invalid_operation():
    with pytest.raises(ValueError):
        calcular('invalid', 1, 1)

def test_calcular_invalid_type():
    with pytest.raises(TypeError):
        calcular('adicionar', 'a', 1)
    with pytest.raises(TypeError):
        calcular('subtrair', 1, 'b')