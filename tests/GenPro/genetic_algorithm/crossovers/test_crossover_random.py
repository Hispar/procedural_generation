# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
from src.GenPro.genetic_algorithm.crossovers.crossover_random import CrossoverRandom
from src.GenPro.genetic_algorithm.individual import Individual
from src.GenPro.genetic_algorithm.individuals.basic import BasicIndividual


def test_create_crossover_random():
    crossover = CrossoverRandom()
    assert hasattr(crossover, 'parent_a') is False
    assert hasattr(crossover, 'parent_b') is False


def test_crossover_random_create_offspring():
    crossover = CrossoverRandom()
    parent = Individual()
    crossover.set_parents(parent, parent)
    individual = crossover.create_offspring()
    assert individual.genes_list == []


def test_crossover_random_create_offspring_basic_individual():
    crossover = CrossoverRandom(individual_class=BasicIndividual)
    parent = BasicIndividual()
    crossover.set_parents(parent, parent)
    individual = crossover.create_offspring()
    assert type(individual) == BasicIndividual
    assert individual.genes_list == []


def test_crossover_random_create_offspring_basic_individual_with_genes():
    crossover = CrossoverRandom(individual_class=BasicIndividual)
    parent = BasicIndividual(gen1=1, gen2=2)
    crossover.set_parents(parent, parent)
    individual = crossover.create_offspring()
    assert type(individual) == BasicIndividual
    assert parent.genes_list == ['gen1', 'gen2']
    assert individual.genes_list == ['gen1', 'gen2']
    assert individual.gen1 == 1
    assert individual.gen2 == 2


def test_crossover_random_create_offspring_basic_individual_with_genes_different_parents():
    crossover = CrossoverRandom(individual_class=BasicIndividual)
    parent_a = BasicIndividual(gen1=1, gen2=2)
    parent_b = BasicIndividual(gen1=3, gen2=4)
    crossover.set_parents(parent_a, parent_b)
    individual = crossover.create_offspring()
    assert type(individual) == BasicIndividual
    assert parent_a.genes_list == ['gen1', 'gen2']
    assert parent_b.genes_list == ['gen1', 'gen2']
    assert individual.genes_list == ['gen1', 'gen2']
    assert individual.gen1 in [1, 3]
    assert individual.gen2 in [2, 4]
