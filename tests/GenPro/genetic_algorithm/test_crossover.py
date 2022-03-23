# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
import pytest

from src.GenPro.genetic_algorithm.crossover import Crossover
from src.GenPro.genetic_algorithm.individual import Individual


def test_create_crossover():
    crossover = Crossover()
    assert hasattr(crossover, 'parent_a') is False
    assert hasattr(crossover, 'parent_b') is False


def test_crossover_set_parents():
    crossover = Crossover()
    parent = Individual()
    crossover.set_parents(parent, parent)
    assert hasattr(crossover, 'parent_a') is True
    assert hasattr(crossover, 'parent_b') is True
    assert crossover.parent_a is parent
    assert crossover.parent_b is parent


def test_crossover_create_offspring():
    crossover = Crossover()
    with pytest.raises(NotImplementedError):
        crossover.create_offspring()
