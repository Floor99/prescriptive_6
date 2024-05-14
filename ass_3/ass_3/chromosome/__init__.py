import pandas as pd
from ass_3.gene import EngineGene
from ass_3.utils import select_engines_for_maintenance



class Chromosome:
    all_engines = pd.read_csv('ass_3/data/RUL_consultancy_predictions_A3-2.csv', sep = ";")
    engines_for_maintenance = select_engines_for_maintenance(all_engines, 29)
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
        self.engine_gene_elements = [self.bits[i:i+7] for i in range(0, len(self.bits), 7)]
        self.engine_genes = [EngineGene(id, self.engine_gene_elements[i]) for i, id in enumerate(self.maintenance_ids)]
        self.engine_ids = [gene.engine_id for gene in self.engine_genes]
    
    def get_penalty(self) -> None:
        """
        Calculate the penalty associated with the chromosome.

        This method sums up the penalties of all engine genes in the chromosome.

        Returns:
        - None
        """
        
        self.penalty = sum([engine_gene.penalty.penalty for engine_gene in self.engine_genes])
    
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(bits={self.bits!r},\n engine_genes={self.engine_genes!r},\n penalty={self.penalty!r})"