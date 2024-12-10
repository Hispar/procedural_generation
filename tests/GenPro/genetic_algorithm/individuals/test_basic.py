import pytest

from src.GenPro.genetic_algorithm.individuals.basic import BasicIndividual


def test_individual_basic_fitness():
    individual = BasicIndividual()
    with pytest.raises(NotImplementedError):
        individual.fitness()


def test_individual_basic_genes():
    individual = BasicIndividual()
    assert individual.genes() == []


def test_individual_basic_with_genes():
    individual = BasicIndividual(gen1=1, gen2=2)
    assert individual.genes() == ['gen1', 'gen2']
    assert individual.gen1 == 1
    assert individual.gen2 == 2
