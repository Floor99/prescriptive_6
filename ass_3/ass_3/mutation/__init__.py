from abc import ABC, abstractmethod
import random

from ass_3.chromosome import Chromosome


class Mutation(ABC):
    """
    Abstract base class representing a mutation operation on chromosomes.

    Methods:
    - mutate(): Abstract method for mutating a chromosome.

    Parameters:
    - chromosome (Chromosome): The chromosome to be mutated.

    Returns:
    - Chromosome: The mutated chromosome.
    """
    
    @abstractmethod
    def mutate(self):
        """
        Abstract method for mutating a chromosome.

        Parameters:
        - chromosome (Chromosome): The chromosome to be mutated.

        Returns:
        - Chromosome: The mutated chromosome.
        """
        pass
    

class UniformCrossMutation(Mutation):
    """
    A class implementing uniform crossover mutation on chromosomes.

    Attributes:
    - mutation_probability (float): Probability of mutation for each bit.

    Methods:
    - __init__(mutation_probability: float): Initialize a UniformCrossMutation object.
    - mutate(chromosome: Chromosome) -> Chromosome: Mutate the chromosome using uniform crossover mutation.
    """
    
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
        Mutate the chromosome using uniform crossover mutation.

        This method mutates the chromosome by flipping bits with a probability defined by the mutation_probability.

        Parameters:
        - chromosome (Chromosome): The chromosome to be mutated.

        Returns:
        - Chromosome: The mutated chromosome.
        """
        # iterate through each bit and flip it with a certain probability 
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

