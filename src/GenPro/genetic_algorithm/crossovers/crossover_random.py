# -*- coding: utf-8 -*-
# Python imports
from random import choice

# 3rd Party imports

# App imports
from ..crossover import Crossover
from ..individual import Individual


class CrossoverRandom(Crossover):

    def create_offspring(self) -> Individual:
        """
        Create offspring choosing randomly genes from his parents
        :return:
        """
        offspring = self.individual_class()
        for gen in self.parent_a.genes():
            parent = choice((self.parent_a, self.parent_b))
            offspring.add_gen(gen, getattr(parent, gen))
        return offspring
