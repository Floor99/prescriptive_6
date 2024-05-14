from abc import ABC, abstractmethod
import random

import numpy as np

from ass_3.chromosome import Chromosome


class CrossOver(ABC):
    """
    Abstract base class representing a crossover operation on chromosomes.

    Methods:
    - cross_over(): Abstract method for performing crossover operation.
    """
    
    @abstractmethod
    def cross_over(self):
        """
        Abstract method for performing crossover operation.
        """
        pass


class SingleCrossOver(CrossOver):
    def cross_over(self, parent1:Chromosome, parent2:Chromosome) -> list[Chromosome]:
        """
        Perform single-point crossover operation.

        Parameters:
        - parent1 (Chromosome): The first parent chromosome.
        - parent2 (Chromosome): The second parent chromosome.

        Returns:
        - list[Chromosome]: List of child chromosomes resulting from the crossover.
        """
        
        crossover_point = np.random.randint(1, len(parent1.bits) - 1 )
        
        child1 = parent1.bits[:crossover_point] + parent2.bits[crossover_point:]
        child2 = parent2.bits[:crossover_point] + parent1.bits[crossover_point:]
        
        return [Chromosome(child1), Chromosome(child2)]


def will_parents_mate(probability:float=0.9):
    """
    Determine if parents will mate based on a given probability.

    Parameters:
    - probability (float, optional): The probability of parents mating. Defaults to 0.9.

    Returns:
    - bool: True if parents will mate, False otherwise.
    """
    r = random.uniform(0, 1)
    if probability < r:
        return False
    return True

