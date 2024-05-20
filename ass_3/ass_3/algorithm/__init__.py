import copy
import time

import numpy as np
from ass_3.chromosome import Chromosome
from ass_3.constraints import Constraint, chromosome_meets_all_constraints
from ass_3.cross_over import CrossOver, will_parents_mate
from ass_3.initialization import Initializer
from ass_3.mutation import Mutation
from ass_3.selection import Selection
from ass_3.termination import Termination



# class GeneticAlgorithm:
#     """
#     A class representing a Genetic Algorithm (GA) for optimization.

#     Attributes:
#     - initializer (Initializer): The initialization strategy for the GA.
#     - termination_strategy (Termination): The termination criteria for the GA.
#     - selection_strategy (Selection): The parent selection strategy for the GA.
#     - crossover_strategy (CrossOver): The crossover strategy for the GA.
#     - mutation_strategy (Mutation): The mutation strategy for the GA.
#     - mating_probability (float): Probability of parents mating during crossover.
#     - constraints (list[Constraint]): List of constraints to be satisfied.

#     Methods:
#     - __init__(initializer: Initializer, termination_strategy: Termination, selection_strategy: Selection,
#                 crossover_strategy: CrossOver, mutation_strategy: Mutation, mating_probability: float,
#                 constraints: list[Constraint]) -> None: Initialize a GeneticAlgorithm object.
#     - run_algorithm(): Run the Genetic Algorithm.
#     """
    
#     def __init__(
#         self,
#         initializer:Initializer,
#         termination_strategy: Termination,
#         selection_strategy: Selection,
#         crossover_strategy: CrossOver,
#         mutation_strategy: Mutation,
#         mating_probability: float,
#         constraints:list[Constraint],
#     ) -> None:
#         """
#         Initialize a GeneticAlgorithm object.

#         Parameters:
#         - initializer (Initializer): The initialization strategy for the GA.
#         - termination_strategy (Termination): The termination criteria for the GA.
#         - selection_strategy (Selection): The parent selection strategy for the GA.
#         - crossover_strategy (CrossOver): The crossover strategy for the GA.
#         - mutation_strategy (Mutation): The mutation strategy for the GA.
#         - mating_probability (float): Probability of parents mating during crossover.
#         - constraints (list[Constraint]): List of constraints to be satisfied.

#         Returns:
#         - None
#         """
        
#         self.initializer = initializer
#         self.termination_strategy = termination_strategy
#         self.selection_strategy = selection_strategy
#         self.crossover_strategy = crossover_strategy
#         self.mutation_strategy = mutation_strategy
#         self.mating_probability = mating_probability
#         self.constraints = constraints

#     def run_algorithm(self):
#         """
#         Run the Genetic Algorithm.

#         Returns:
#         - Chromosome: The best solution found by the GA.
#         """
        
#         population = self.initializer.initialize_population()
        
#         penalties_initial_population = np.array([chromosome.penalty for chromosome in population])
#         print(f"{penalties_initial_population= }") 
#         best_chromosome_index_init_population = np.argmin(penalties_initial_population)
#         best_chromosome_init_population = population[best_chromosome_index_init_population]
              
#         penalty_initial = best_chromosome_init_population.penalty 
        
#         print(f"{penalty_initial= }")
        
#         new_offspring = copy.deepcopy(population)
#         start_time = time.time()
#         while not self.termination_strategy.meets_termination(start_time):
#             to_be_mutated = []
#             selection = self.selection_strategy.select_parents(new_offspring)
#             parent_pairs = [selection[i:i+2] for i in range(0, len(selection), 2)]
            
#             print(f"{[sel.penalty for sel in selection]= }")
#             # for sel in selection:
#             #     print(sel.penalty)
            
#             to_be_mutated.extend(selection)
            
#             while len(to_be_mutated) < len(population):
#                 for pair in parent_pairs:
                    
#                     if not will_parents_mate(self.mating_probability):
#                         continue
#                     else:
#                         # print('Crossover')
                    
                        
#                         childs = self.crossover_strategy.cross_over(pair[0], pair[1])
#                         examined_children = [chromosome_meets_all_constraints(child, self.constraints) for child in childs]
#                         valid_children_indices = [i for i, valid_child in enumerate(examined_children) if valid_child]
#                         valid_children = [childs[child] for child in valid_children_indices]
#                         to_be_mutated.extend(valid_children)
#                         # print(len(to_be_mutated))
#                         # if len(to_be_mutated) > 10:
#                         #     to_be_mutated = to_be_mutated[:10]
#             valid_mutations = []
#             # print('Mutation')
#             for i, chromosome in enumerate(to_be_mutated):
#                 while True: 
#                     mutated = self.mutation_strategy.mutate(chromosome)
#                     if chromosome_meets_all_constraints(mutated, self.constraints):
#                         valid_mutations.append(mutated)
#                         break
#             # print('Mutation ended')

#             new_offspring = valid_mutations
        
            
#         penalties = np.array([chromosome.penalty for chromosome in new_offspring])    
#         best_chromosome_index = np.argmin(penalties)
        
#         return new_offspring[best_chromosome_index]







class GeneticAlgorithm:
    """
    A class representing a Genetic Algorithm (GA) for optimization.

    Attributes:
    - initializer (Initializer): The initialization strategy for the GA.
    - termination_strategy (Termination): The termination criteria for the GA.
    - selection_strategy (Selection): The parent selection strategy for the GA.
    - crossover_strategy (CrossOver): The crossover strategy for the GA.
    - mutation_strategy (Mutation): The mutation strategy for the GA.
    - mating_probability (float): Probability of parents mating during crossover.
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Methods:
    - __init__(initializer: Initializer, termination_strategy: Termination, selection_strategy: Selection,
                crossover_strategy: CrossOver, mutation_strategy: Mutation, mating_probability: float,
                constraints: list[Constraint]) -> None: Initialize a GeneticAlgorithm object.
    - run_algorithm(): Run the Genetic Algorithm.
    """
    
    def __init__(
        self,
        initializer:Initializer,
        termination_strategy: Termination,
        selection_strategy: Selection,
        crossover_strategy: CrossOver,
        mutation_strategy: Mutation,
        mating_probability: float,
        constraints:list[Constraint],
    ) -> None:
        """
        Initialize a GeneticAlgorithm object.

        Parameters:
        - initializer (Initializer): The initialization strategy for the GA.
        - termination_strategy (Termination): The termination criteria for the GA.
        - selection_strategy (Selection): The parent selection strategy for the GA.
        - crossover_strategy (CrossOver): The crossover strategy for the GA.
        - mutation_strategy (Mutation): The mutation strategy for the GA.
        - mating_probability (float): Probability of parents mating during crossover.
        - constraints (list[Constraint]): List of constraints to be satisfied.

        Returns:
        - None
        """
        
        self.initializer = initializer
        self.termination_strategy = termination_strategy
        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.mating_probability = mating_probability
        self.constraints = constraints

    def run_algorithm(self):
        """
        Run the Genetic Algorithm.

        Returns:
        - Chromosome: The best solution found by the GA.
        """
        
        self.initial_population = self.initializer.initialize_population()
        new_offspring = copy.deepcopy(self.initial_population)
        start_time = time.time()
        while not self.termination_strategy.meets_termination(start_time): 
            selection = self.selection_strategy.select_parents(new_offspring)
            # to_be_mutated = copy.deepcopy(selection)
            to_be_mutated = []
            
            # mating_parents = [parent for parent in selection if will_parents_mate(self.mating_probability)]
            mating_parents = []
            for parent in selection:
                if will_parents_mate(self.mating_probability):
                    mating_parents.append(parent)
                else:
                    to_be_mutated.append(parent)
    
            even_mating_parents = self.get_even_amount_of_parents_(mating_parents)
            parent_pairs = [even_mating_parents[i:i+2] for i in range(0, len(even_mating_parents), 2)]
            

            while len(to_be_mutated) < len(self.initial_population):
                for pair in parent_pairs:
                    children = self.crossover_strategy.cross_over(pair[0], pair[1])
                    valid_children = self.get_valid_chromosomes_(children)
                    to_be_mutated.extend(valid_children)
            # print("mutation")
            
            
            if self.mutation_strategy.mutation_probability:
                new_offspring = copy.deepcopy(even_mating_parents)
                while len(new_offspring) < len(self.initial_population):
                    mutations = [self.mutation_strategy.mutate(chromosome) for chromosome in to_be_mutated]
                    valid_mutations = self.get_valid_chromosomes_(mutations)
                    new_offspring.extend(valid_mutations)
            else:
                new_offspring = copy.deepcopy(to_be_mutated)

                    
        return new_offspring


    def get_even_amount_of_parents_(self, parents:list[Chromosome]):
        parents = parents.copy()
        if not len(parents)%2 == 0:
                parents = parents[:-1]
        return parents


    def get_valid_chromosomes_(self, chromosomes: list[Chromosome]) -> list[Chromosome]:
        examined_chromosomes = [chromosome_meets_all_constraints(chromosome, self.constraints) for chromosome in chromosomes]
        valid_chromosome_indices = [i for i, valid_chromosome in enumerate(examined_chromosomes) if valid_chromosome]
        valid_chromosomes = [chromosomes[chromosome] for chromosome in valid_chromosome_indices]
        return valid_chromosomes
    
    
    def get_best_chromosome(self, chromosomes:list[Chromosome]):
        penalties = np.array([chromosome.penalty for chromosome in chromosomes])
        best_chromosome_index = np.argmin(penalties)
        best_chromosome = chromosomes[best_chromosome_index]
        return best_chromosome
    
    
