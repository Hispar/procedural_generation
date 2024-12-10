from ..crossover import Crossover
from ..individual import Individual


class CrossoverTwoPoints(Crossover):
    crossover_point_1: int = 0
    crossover_point_2: int = 0

    def set_crossover_points(self, crossover_point_1: int, crossover_point_2: int):
        self.crossover_point_1 = crossover_point_1
        self.crossover_point_2 = crossover_point_2

    def create_offspring(self) -> Individual:
        """
        Create offspring choosing genes from one parent between crossover points
        :return:
        """
        offspring = Individual()
        crossover_point = 0
        parent = self.parent_a
        for gen in self.parent_a.genes_list:
            if self.crossover_point_2 >= crossover_point > self.crossover_point_1:
                parent = self.parent_b
            offspring.__setattr__(gen, parent.__getattribute__(gen))
            crossover_point += 1
        return offspring
