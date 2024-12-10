from .individual import Individual


class Crossover:
    parent_a: Individual
    parent_b: Individual
    individual_class: type

    def __init__(self, individual_class: type = Individual):
        self.individual_class = individual_class

    def set_parents(self, parent_a: Individual, parent_b: Individual):
        self.parent_a = parent_a
        self.parent_b = parent_b

    def create_offspring(self) -> Individual:
        raise NotImplementedError
