from abc import ABC, abstractmethod
import copy
from ass_3.chromosome import Chromosome



class Constraint(ABC):
    """
    Abstract base class representing a constraint on chromosomes.

    Methods:
    - meets_constraint(): Abstract method for checking if a chromosome meets the constraint.
    """
    
    @abstractmethod
    def meets_constraint(self):
        """
        Abstract method for checking if a chromosome meets the constraint.
        """
        pass 

class Day31Constraint(Constraint):
    def meets_constraint(self, chromosome: Chromosome):
        """
        Check if the chromosome has start_day of 31 (which is outside of the planning period, and cannot be part of the chromosome).

        Parameters:
        - chromosome (Chromosome): The chromosome to be checked.

        Returns:
        - bool: True if the chromosome meets the day 31 constraint, False otherwise.
        """
        
        for engine_gene in chromosome.engine_genes:
            if engine_gene.start_day == 31:
                return False 
        
        return True
    
class CompletesMaintenanceIn30Days(Constraint):
    def meets_constraint(self, chromosome: Chromosome):
        """
        A constraint ensuring that maintenance of all engine genes completes within 30 days.
        Check if the chromosome meets the completion within 30 days constraint.

        Parameters:
        - chromosome (Chromosome): The chromosome to be checked.

        Returns:
        - bool: True if the chromosome meets the completion within 30 days constraint, False otherwise.
        """
        
        for engine_gene in chromosome.engine_genes:
            if engine_gene.start_day.start_day + engine_gene.maintenance_time > 30:
                return False 
        
        return True 

class TeamWorksAtOneEngine(Constraint):
    def meets_constraint(self, chromosome: Chromosome):
        """
        A constraint ensuring that a team works on only one engine at a time.
        Check if the chromosome meets the one-engine-per-team constraint.

        Parameters:
        - chromosome (Chromosome): The chromosome to be checked.

        Returns:
        - bool: True if the chromosome meets the one-engine-per-team constraint, False otherwise.
        """
        
        for i, _ in enumerate(chromosome.engine_genes):
            remainder = copy.deepcopy(chromosome.engine_genes[i:])
            engine_gene = remainder.pop(0)
            for rem_engine_gene in remainder:
                if engine_gene.team == rem_engine_gene.team:
                    if rem_engine_gene.start_day < (engine_gene.start_day + engine_gene.maintenance_time) or rem_engine_gene.start_day > (engine_gene.start_day - rem_engine_gene.maintenance_time):
                        return False
        return True
    
        
def chromosome_meets_all_constraints(chromosome:Chromosome, constraints:list[Constraint]):
    """
    Check if a chromosome meets all given constraints.

    Parameters:
    - chromosome (Chromosome): The chromosome to be checked.
    - constraints (list[Constraint]): List of constraints to be satisfied.

    Returns:
    - bool: True if the chromosome meets all constraints, False otherwise.
    """
    
    for constraint in constraints:
        if not constraint.meets_constraint(chromosome):
            return False
    
    return True


