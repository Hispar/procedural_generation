# -*- coding: utf-8 -*-
# Python imports
from random import sample
from typing import List

# 3rd Party imports

# App imports
from ..crossover import Crossover
from ..individual import Individual


class CrossoverMultiPoints(Crossover):
    number_of_crossover_points: int = 1
    crossover_points: List[int]

    def set_number_of_crossover_points(self, number_of_crossover_points: int):
        self.number_of_crossover_points = number_of_crossover_points

    def generate_crossover_points(self):
        total_genes = len(self.parent_a.genes_list)
        self.crossover_points = sample([n for n in range(total_genes)], self.number_of_crossover_points)
        self.crossover_points.sort()
        self.crossover_points.reverse()

    def create_offspring(self) -> Individual:
        """
        Create offspring choosing genes from one parent between crossover points
        :return:
        """
        offspring = Individual()
        self.generate_crossover_points()
        base_point = self.crossover_points.pop()
        crossover_point = 0
        parent = self.parent_a
        for gen in self.parent_a.genes_list:
            if self.crossover_point_2 > crossover_point > self.crossover_point_1:
                parent = self.parent_b
            offspring.__setattr__(gen, parent.__getattribute__(gen))
            crossover_point += 1
        return offspring
