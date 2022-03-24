# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
from src.GenPro.genetic_algorithm.algorithm import GeneticAlgorithm
from src.GenPro.genetic_algorithm.crossover import Crossover
from src.GenPro.genetic_algorithm.individual import Individual


def test_genetic_algorithm_creation():
    population = [Individual()]
    config = GeneticAlgorithm.InitialInput(
        population=population
    )
    algorithm = GeneticAlgorithm(config)

    assert algorithm.population == population
    assert algorithm.max_offspring == 2
    assert type(algorithm.crossover) == Crossover


def test_genetic_algorithm_set_crossover_method():
    population = [Individual()]
    config = GeneticAlgorithm.InitialInput(
        population=population
    )
    algorithm = GeneticAlgorithm(config)
    crossover = Crossover()

    algorithm.set_crossover_method(crossover=crossover)
    assert algorithm.crossover == crossover


def test_genetic_algorithm_offspring_count_no_fixed():
    population = [Individual()]
    config = GeneticAlgorithm.InitialInput(
        population=population
    )
    algorithm = GeneticAlgorithm(config)

    assert hasattr(algorithm, 'fixed_offspring') is False
    assert algorithm.offspring_count() in [i + 1 for i in range(algorithm.max_offspring)]


def test_genetic_algorithm_offspring_count_fixed():
    population = [Individual()]
    config = GeneticAlgorithm.InitialInput(
        population=population
    )
    algorithm = GeneticAlgorithm(config)
    algorithm.fixed_offspring = 2

    assert algorithm.offspring_count() == 2
