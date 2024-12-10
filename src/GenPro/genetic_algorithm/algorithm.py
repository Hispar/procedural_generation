from dataclasses import dataclass
from random import randint
from typing import Tuple, List, Optional

from .crossover import Crossover
from .individual import Individual


class GeneticAlgorithm:
    population: List[Individual]
    crossover: Crossover
    max_offspring: Optional[int]
    fixed_offspring: Optional[int]

    @dataclass
    class InitialInput:
        """
        Initial input configuration of the algorithm
        """
        population: List[Individual]
        crossover: Crossover = Crossover()
        max_offspring: int = 2

    @dataclass
    class CrossoverInitialInput:
        """
        Crossover input configuration
        """
        parents: Optional[Tuple[Individual, Individual]]
        max_offspring: Optional[int]
        fixed_offspring: Optional[int]

    def __init__(self, initial: InitialInput):
        self.population = initial.population
        self.max_offspring = initial.max_offspring
        self.crossover = initial.crossover

    def set_crossover_method(self, crossover: Crossover):
        self.crossover = crossover

    def selection(self) -> Tuple[Individual, Individual]:
        """
        Select the two most fitted individuals to crossover
        :return:
        """
        individual_a, individual_b = sorted(self.population, key=lambda individual: individual.fitness())[:2]
        return individual_a, individual_b

    def set_crossover_config(self, config: CrossoverInitialInput):
        if config.parents:
            self.crossover.set_parents(config.parents[0], config.parents[1])
        else:
            individual_a, individual_b = self.selection()
            self.crossover.set_parents(individual_a, individual_b)
        if config.max_offspring:
            self.max_offspring = config.max_offspring
        if config.fixed_offspring:
            self.fixed_offspring = config.fixed_offspring

    def crossover(self, config: CrossoverInitialInput):
        self.set_crossover_config(config=config)
        for i in range(self.offspring_count()):
            individual = self.crossover.create_offspring()
            self.add_population(individual)

    def offspring_count(self):
        if hasattr(self, 'fixed_offspring') and self.fixed_offspring:
            return self.fixed_offspring

        return randint(1, self.max_offspring)

    def add_population(self, individual: Individual):
        self.population.append(individual)
