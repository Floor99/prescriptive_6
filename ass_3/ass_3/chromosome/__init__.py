import pandas as pd
from ass_3.gene import EngineGene
from ass_3.utils import select_engines_for_maintenance



class Chromosome:
    """
    A class representing a Chromosome object.

    Attributes:
    - all_engines (DataFrame): DataFrame containing all engine data.
    - engines_for_maintenance (DataFrame): DataFrame containing engines selected for maintenance.
    - maintenance_ids (list): List of IDs of engines selected for maintenance.

    Methods:
    - __init__(bits:list[int]) -> None: Initialize a Chromosome object.
    - decode_bits() -> None: Decode the bit representation of the chromosome.
    - get_penalty() -> None: Calculate the penalty associated with the chromosome.
    - __repr__() -> str: Return a string representation of the Chromosome object.
    """
    
    # Read all engines data with RUL and ids
    all_engines = pd.read_csv('ass_3/data/RUL_consultancy_predictions_A3-2.csv', sep = ";")
    # Select the engines with a safety date less than 29 - the ones that need maintenance 
    engines_for_maintenance = select_engines_for_maintenance(all_engines, 29)
    # Get ids of engines that are selected for maintenance
    maintenance_ids = engines_for_maintenance["id"].tolist()


    def __init__(self, bits:list[int]) -> None:
        """
        Initialize a Chromosome object.

        Parameters:
        - bits (list[int]): List of bits representing the chromosome.

        Returns:
        - None
        """
        
        self.bits = bits
        self.decode_bits()
        self.get_penalty()

    
    def decode_bits(self) -> None:
        """
        Decode the bit representation of the chromosome.

        This method divides the bit representation into engine gene elements and creates EngineGene objects
        for each element.

        Returns:
        - None
        """
        
        # split the bit representation into engine gene elements
        self.engine_gene_elements = [self.bits[i:i+7] for i in range(0, len(self.bits), 7)]
        
        # create EngineGene objects for each element
        self.engine_genes = [EngineGene(id, self.engine_gene_elements[i]) for i, id in enumerate(self.maintenance_ids)]
        
        # get ids of engine genes 
        self.engine_ids = [gene.engine_id for gene in self.engine_genes]
    
    def get_penalty(self) -> None:
        """
        Calculate the penalty associated with the chromosome.

        This method sums up the penalties of all engine genes in the chromosome.

        Returns:
        - None
        """
        
        # sum up the penalties of all enginge genes -> penalties for total chromosome
        self.penalty = sum([engine_gene.penalty.penalty for engine_gene in self.engine_genes])
    
    
    def __repr__(self):
        """
        Return a string representation of the Chromosome object.

        Returns:
        - str: String representation of the Chromosome object.
        """
        
        class_name = type(self).__name__
        return f"{class_name}(bits={self.bits!r},\n engine_genes={self.engine_genes!r},\n penalty={self.penalty!r})"