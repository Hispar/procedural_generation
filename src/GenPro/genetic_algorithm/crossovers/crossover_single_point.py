from ..crossover import Crossover
from ..individual import Individual


class CrossoverSinglePoint(Crossover):
    crossover_point: int = 0

    def set_crossover_point(self, crossover_point: int):
        self.crossover_point = crossover_point

    def create_offspring(self) -> Individual:
        """
        Create offspring choosing genes from one parent until the crossover point
        :return:
        """
        offspring = self.individual_class()
        crossover_point = 0
        parent = self.parent_a
        for gen in self.parent_a.genes_list:
            if crossover_point >= self.crossover_point:
                parent = self.parent_b
            offspring.add_gen(gen, getattr(parent, gen))
            crossover_point += 1
        return offspring
