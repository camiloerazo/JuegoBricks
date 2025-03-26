import pytest
from src.calculadora import numero_fibonacci

def test_numero_fibonacci():
    assert numero_fibonacci(0) == 0
    assert numero_fibonacci(1) == 1
    assert numero_fibonacci(5) == 5
    assert numero_fibonacci(10) == 55
    with pytest.raises(ValueError):
        numero_fibonacci(-3)  # Negative numbers should raise an error