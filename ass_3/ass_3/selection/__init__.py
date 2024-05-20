from abc import ABC, abstractmethod
import random
import numpy as np
from ass_3.chromosome import Chromosome


class Selection(ABC):
    """
    Abstract base class representing a selection operation on a population of chromosomes.

    Methods:
    - select_parents(population: list[Chromosome]) -> list[Chromosome]: Abstract method for selecting parents from a population.
    """
    
    @abstractmethod
    def select_parents(self):
        """
        Abstract method for selecting parents from a population.

        Parameters:
        - population (list[Chromosome]): List of Chromosome objects representing the population.

        Returns:
        - list[Chromosome]: List of selected parent Chromosome objects.
        """
        pass


class RouletteWheelSelection(Selection):
    """
    A class implementing roulette wheel selection for selecting parents from a population.

    Attributes:
    - nr_of_parents (int): Number of parents to be selected.
    - modulo_two (bool): If True, ensures the number of selected parents is even.

    Methods:
    - __init__(nr_of_parents: int, modulo_two: bool=True) -> None: Initialize a RouletteWheelSelection object.
    - select_parents(population: list[Chromosome]) -> list[Chromosome]: Select parents from the population using roulette wheel selection.
    """
    
    def __init__(self, nr_of_parents:int) -> None:
        """
        Initialize a RouletteWheelSelection object.

        Parameters:
        - nr_of_parents (int): Number of parents to be selected.
        - modulo_two (bool, optional): If True, ensures the number of selected parents is even. Defaults to True.

        Returns:
        - None
        """
        self.nr_of_parents = nr_of_parents

    
    def select_parents(self, population:list[Chromosome]) -> list[Chromosome]:
        """
        Select parents from the population using roulette wheel selection.
        This method selects parents from the population based on their fitness values using roulette wheel selection.

        Parameters:
        - population (list[Chromosome]): List of Chromosome objects representing the population.

        Returns:
        - list[Chromosome]: List of selected parent Chromosome objects.
        """
        population = population.copy()
        # ensure number of parents is an even number 
        if not self.nr_of_parents%2 == 0:
            self.nr_of_parents -= 1
        
        # print(f"{population= }")
        # calculate fitness values based on penalties
        penalties = [chromosome.penalty for chromosome in population]
        print(f"{penalties= }")
        inverted_values = [1.0 / (1 + penalty) for penalty in penalties]
        # print(f"{inverted_values= }")
        probabilities = (np.array(inverted_values) / sum(inverted_values))*100
        print(f"{probabilities= }")
        
        # select parent indices based on probabilities
        parents_indices = np.random.choice(len(population), size = self.nr_of_parents, p=probabilities, replace=False)
        # print(f"{parents_indices= }")
        parents = [population[i] for i in parents_indices]
        # print(f"{parents= }")
        # print(len(parents))
        
        # ensure that number of parents is an even number
        if not len(parents)%2 == 0:
            parents = parents[:-1]
            print(f"{parents= }")
        return parents