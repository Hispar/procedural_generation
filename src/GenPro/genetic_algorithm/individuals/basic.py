# -*- coding: utf-8 -*-
# Python imports
from typing import List

# 3rd Party imports

# App imports
from ..individual import Individual


class BasicIndividual(Individual):

    def __init__(self, *args, **kwargs):
        super(BasicIndividual, self).__init__(*args, **kwargs)
        for gen, value in kwargs.items():
            self.add_gen(gen, value)

    def fitness(self) -> int:
        """
        Determines how fit an individual is competing with other individuals.
        :return:
        """
        raise NotImplementedError
