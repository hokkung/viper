import pytest
from processor.utils import sum

def test_sum() -> None:
    mock = [1, 2, 3, 4, 5]
    
    assert sum(mock) == 15
