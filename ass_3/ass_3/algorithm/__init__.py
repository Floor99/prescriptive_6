import copy
import time

import numpy as np
from ass_3.constraints import Constraint, chromosome_meets_all_constraints
from ass_3.cross_over import CrossOver, will_parents_mate
from ass_3.initialization import Initializer
from ass_3.mutation import Mutation
from ass_3.selection import Selection
from ass_3.termination import Termination



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
        
        population = self.initializer.initialize_population()
        new_offspring = copy.deepcopy(population)
        start_time = time.time()
        while not self.termination_strategy.meets_termination(start_time):
            to_be_mutated = []
            selection = self.selection_strategy.select_parents(new_offspring)
            parent_pairs = [selection[i:i+2] for i in range(0, len(selection), 2)]
            for pair in parent_pairs:
                to_be_mutated.extend(pair)
                if not will_parents_mate(self.mating_probability):
                    continue
                else:
                    while len(to_be_mutated) < len(new_offspring):
                        childs = self.crossover_strategy.cross_over(pair[0], pair[1])
                        examined_children = [chromosome_meets_all_constraints(child, self.constraints) for child in childs]
                        valid_children_indices = [i for i, valid_child in enumerate(examined_children) if valid_child]
                        valid_children = [childs[child] for child in valid_children_indices]
                        # print(valid_children)
                        # print("======================")
                        to_be_mutated.extend(valid_children)
            valid_mutations = []
            for i, chromosome in enumerate(to_be_mutated):
                # print(i)
                while True: 
                    mutated = self.mutation_strategy.mutate(chromosome)
                    if chromosome_meets_all_constraints(mutated, self.constraints):
                        valid_mutations.append(mutated)
                        break
            # print("Mutation ended")

            new_offspring = valid_mutations
            # new_offspring = to_be_mutated
        
            
        penalties = np.array([chromosome.penalty for chromosome in new_offspring])    
        best_chromosome_index = np.argmin(penalties)
        return new_offspring[best_chromosome_index]



