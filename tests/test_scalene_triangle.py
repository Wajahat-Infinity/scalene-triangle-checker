import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scalene_triangle import is_scalene_triangle  # Importing directly from scalene_triangle.py

def test_scalene_triangle_true():
    assert is_scalene_triangle(3, 4, 5) == True

def test_scalene_triangle_false():
    assert is_scalene_triangle(2, 2, 3) == False

def test_scalene_triangle_invalid_input():
    with pytest.raises(ValueError):
        is_scalene_triangle(-1, 2, 3)

