import pytest

from src.GenPro.genetic_algorithm.individual import Individual


def test_individual_fitness():
    individual = Individual()
    with pytest.raises(NotImplementedError):
        individual.fitness()


def test_individual_genes():
    individual = Individual()
    assert individual.genes() == []


def test_individual_add_gen():
    individual = Individual()
    individual.add_gen('gen1', 'value1')
    assert individual.genes() == ['gen1']
    assert individual.gen1 == 'value1'
