# -*- coding: utf-8 -*-
# Python imports
from dataclasses import dataclass
from typing import Tuple, List

# 3rd Party imports

# App imports
from .crossover import Crossover
from .individual import Individual


class GeneticAlgorithm:
    @dataclass
    class InitialInput:
        """
        Initial input configuration of the algorithm
        """
        population: List[Individual]
        crossover: Crossover = Crossover()
        max_offspring: int = 2

    def __init__(self, initial: InitialInput):
        self.population = initial.population
        self.max_offspring = initial.max_offspring
        self.crossover = initial.crossover

    def selection(self) -> Tuple[Individual, Individual]:
        """
        Select the two most fitted individuals to crossover
        :return:
        """
        individuals = sorted(self.population, key=lambda individual: individual.fitness())[:2]
        return individuals[0], individuals[1]

    def crossover(self, parent_a: Individual, parent_b: Individual) -> List[Individual]:
        self.crossover.set_parents(parent_a, parent_b)
        for i in range(self.max_offspring):
            individual = self.crossover.create_offspring()
            self.add_population(individual)

    def add_population(self, individual: Individual):
        self.population.append(individual)
