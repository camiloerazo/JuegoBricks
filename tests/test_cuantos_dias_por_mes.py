import pytest
from src.calculadora import dias_en_mes

def test_dias_en_mes():
    assert dias_en_mes(1, 2024) == 31
    assert dias_en_mes(2, 2024) == 29  
    assert dias_en_mes(2, 2023) == 28  
    assert dias_en_mes(4, 2022) == 30  
    assert dias_en_mes(12, 2025) == 31  
    with pytest.raises(ValueError):
        dias_en_mes(0, 2024)  # Invalid month
    with pytest.raises(ValueError):
        dias_en_mes(13, 2024)  # Invalid month