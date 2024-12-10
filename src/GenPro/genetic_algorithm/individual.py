from typing import List


class Individual:
    genes_list: List[str]

    def __init__(self, *args, **kwargs):
        self.genes_list = []

    def fitness(self) -> int:
        """
        Determines how fit an individual is competing with other individuals.
        :return:
        """
        raise NotImplementedError

    def genes(self) -> List[str]:
        """
        Genes are attributes which can be inherited by the offspring
        :return:
        """
        return self.genes_list

    def add_gen(self, key, value):
        self.genes_list.append(key)
        setattr(self, key, value)

    # def get_gen(self, key):
    #
