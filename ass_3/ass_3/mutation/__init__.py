from abc import ABC, abstractmethod
import random

from ass_3.chromosome import Chromosome


class Mutation(ABC):
    @abstractmethod
    def mutate(self):
        """
        Abstract method for mutating a population of chromosomes.

        Parameters:
        - population (list[Chromosome]): List of Chromosome objects representing the population.

        Returns:
        - list[Chromosome]: List of mutated Chromosome objects.
        """
        pass
    

class UniformCrossMutation(Mutation):
    def __init__(self, mutation_probability:float) -> None:
        """
        Initialize a UniformCrossMutation object.

        Parameters:
        - mutation_probability (float): Probability of mutation for each bit.

        Returns:
        - None
        """
        self.mutation_probability = mutation_probability
        
    def mutate(self, chromosome:Chromosome):
        """
        Mutate the population using uniform crossover mutation.

        This method mutates the population by flipping bits with a probability defined by the mutation_probability.

        Parameters:
        - population (list[Chromosome]): List of Chromosome objects representing the population.

        Returns:
        - list[Chromosome]: List of mutated Chromosome objects.
        """

        bits = chromosome.bits
        for i, bit in enumerate(bits):
            r = random.uniform(0, 1)
            if self.mutation_probability > r:
                bits[i] = flip_bit(bit)
            else: 
                continue
        
        return Chromosome(bits)
            


def flip_bit(bit:int):
    """
    Flip the value of a bit.

    Parameters:
    - bit (int): The bit to be flipped.

    Returns:
    - int: The flipped bit.
    """
    
    if bit > 0:
        bit = 0
    else:
        bit = 1
    
    return bit

