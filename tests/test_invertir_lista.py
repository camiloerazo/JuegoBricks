import pytest
from src.calculadora import invertir_lista

def test_invertir_lista():
    assert invertir_lista([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert invertir_lista([]) == []  # Edge case: empty list
    assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
    assert invertir_lista([True, False, True]) == [True, False, True]