from abc import ABC, abstractmethod
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
    
    def __init__(self, nr_of_parents:int, modulo_two:bool=True) -> None:
        """
        Initialize a RouletteWheelSelection object.

        Parameters:
        - nr_of_parents (int): Number of parents to be selected.
        - modulo_two (bool, optional): If True, ensures the number of selected parents is even. Defaults to True.

        Returns:
        - None
        """
        self.nr_of_parents = nr_of_parents
        self.modulo_two = modulo_two

    
    def select_parents(self, population:list[Chromosome]) -> list[Chromosome]:
        """
        Select parents from the population using roulette wheel selection.
        This method selects parents from the population based on their fitness values using roulette wheel selection.

        Parameters:
        - population (list[Chromosome]): List of Chromosome objects representing the population.

        Returns:
        - list[Chromosome]: List of selected parent Chromosome objects.
        """
        # ensure number of parents is an even number 
        if not self.nr_of_parents%2 == 0:
            self.nr_of_parents -= 1
        
        # calculate fitness values based on penalties
        penalties = [chromosome.penalty for chromosome in population]
        inverted_values = [1.0 / penalty for penalty in penalties]
        probabilities = np.array(inverted_values) / sum(inverted_values)
        
        # select parent indices based on probabilities
        parents_indices = np.random.choice(len(population), size = self.nr_of_parents, p=probabilities, replace=False)
        parents = [population[i] for i in parents_indices]
        
        # ensure that number of parents is an even number
        if self.modulo_two:
            if not len(parents)%2 == 0:
                parents = parents[:-1]
        return parents