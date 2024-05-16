import random
from ass_3.chromosome import Chromosome
from ass_3.constraints import Constraint, chromosome_meets_all_constraints
from ass_3.gene import EngineGene
from concurrent.futures import ProcessPoolExecutor


random.seed(1)

def create_random_chromosome(nr_of_bits:int) -> Chromosome:
    """
    Create a random Chromosome object.

    Parameters:
    - nr_of_bits (int): The number of bits in the chromosome.

    Returns:
    - Chromosome: A random Chromosome object.
    """
    # generate a list of random bits and create a Chromosome object
    bits_string = list(f'{random.getrandbits(nr_of_bits):=0{nr_of_bits}b}')
    bits = list(map(int, bits_string))
    chromosome = Chromosome(bits)
    return chromosome


def create_valid_chromosome(nr_of_bits:int, constraints:list[Constraint]) -> Chromosome:
    """
    Create a valid Chromosome object that meets the given constraints.

    Parameters:
    - nr_of_bits (int): The number of bits in the chromosome.
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Returns:
    - Chromosome: A valid Chromosome object that satisfies the constraints.
    """
    # keep generating random chromosome until a valid (meets all contraints) one is found
    while True:
        chromosome = create_random_chromosome(nr_of_bits)
        if chromosome_meets_all_constraints(chromosome, constraints):
            print("hell yeaaaah!")
            break
        
    return chromosome


def build_valid_chromosome(nr_of_bits:int, constraints:list[Constraint]) -> Chromosome:
    nr_of_engine_gene_bits = 7
    nr_of_engine_genes = nr_of_bits/nr_of_engine_gene_bits
    
    chromosome_bits = []
    retries = 0
    while len(chromosome_bits) < nr_of_bits:
        engine_gene_bits_string = list(f'{random.getrandbits(nr_of_engine_gene_bits):=0{nr_of_engine_gene_bits}b}')
        engine_gene_bits = list(map(int, engine_gene_bits_string))
        chromosome_bits.extend(engine_gene_bits)
        chromosome = Chromosome(chromosome_bits)
        if not chromosome_meets_all_constraints(chromosome, constraints):
            chromosome_bits = chromosome_bits[:-7]
            retries+=1
            if retries > 100:
                chromosome_bits = remove_random_gene(chromosome_bits)
                retries = 0
            # if retries > 1000:
            #     break
        # print(len(chromosome_bits))
    return chromosome


def remove_random_gene(bits:list):

    # Define the starting indices for each group of 7 bits
    indices = list(range(0, len(bits), 7))

    # Choose a random starting index
    start_index = random.choice(indices)

    # Extract the 7-bit sample
    del bits[start_index:start_index + 7]
    return bits


def set_random_gene_to_zero(bits:list):
    # Define the starting indices for each group of 7 bits
    indices = list(range(0, len(bits), 7))

    # Choose a random starting index
    start_index = random.choice(indices)

    # Extract the 7-bit sample
    bits[start_index+2:start_index + 7] = [0]*5
    return bits


def initialize_population(population_size:int, nr_of_bits:int, constraints:list[Constraint]) -> list[Chromosome]:
    """
    Initialize a population of Chromosome objects that are valid (meets all contstraints).

    Parameters:
    - population_size (int): The size of the population.
    - nr_of_bits (int): The number of bits in each chromosome (7 bits per engine).
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Returns:
    - list[Chromosome]: A list of Chromosome objects representing the initialized population.
    """
    with ProcessPoolExecutor(10) as exe:
        population = [popu for popu in exe.map(build_valid_chromosome, [nr_of_bits]*population_size, [constraints]*population_size)]
    # population = [build_valid_chromosome(nr_of_bits, constraints) for _ in range(population_size)]
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
        - list[Chromosome]: A list of Chromosome objects representing the initialized population.
        """

        return initialize_population(self.population_size, self.chromosome_length, self.constraints)
        

