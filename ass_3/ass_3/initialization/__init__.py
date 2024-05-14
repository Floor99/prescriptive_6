
import random
from ass_3.chromosome import Chromosome
from ass_3.constraints import Constraint, chromosome_meets_all_constraints


def create_random_chromosome(nr_of_bits:int, constraints:list[Constraint]) -> Chromosome:
    """
    Create a random Chromosome object that meets the given constraints.

    Parameters:
    - nr_of_bits (int): The number of bits in the chromosome.
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Returns:
    - Chromosome: A random Chromosome object that satisfies the constraints.
    """
    
    bits_string = list(f'{random.getrandbits(nr_of_bits):=0{nr_of_bits}b}')
    bits = list(map(int, bits_string))
    chromosome = Chromosome(bits)
    return chromosome


def create_valid_chromosome(nr_of_bits:int, constraints:list[Constraint]) -> Chromosome:
    while True:
        chromosome = create_random_chromosome(nr_of_bits, constraints)
        if chromosome_meets_all_constraints(chromosome, constraints):
            break
    return chromosome


def initialize_population(population_size:int, nr_of_bits:int, constraints:list[Constraint]) -> list[Chromosome]:
    """
    Initialize a population of Chromosome objects.

    Parameters:
    - population_size (int): The size of the population.
    - nr_of_bits (int): The number of bits in each chromosome (7 bits per engine).
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Returns:
    - list[Chromosome]: A list of Chromosome objects representing the initialized population.
    """
    
    population = [create_valid_chromosome(nr_of_bits, constraints) for _ in range(population_size)]
    return population


class Initializer:
    def __init__(self, chromosome_length, population_size, constraints) -> None:
        """
        Initialize an Initializer object.

        Parameters:
        - chromosome_length (int): The length of each chromosome.
        - population_size (int): The size of the population.
        - constraints (list): List of constraints to be satisfied.

        Returns:
        - None
        """
        
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.constraints = constraints
    
    def initialize_population(self):
        """
        Initialize the population based on the provided parameters.

        Returns:
        - None
        """
        
        # self.population = initialize_population(self.population_size, self.chromosome_length, self.constraints)
        return initialize_population(self.population_size, self.chromosome_length, self.constraints)
        

