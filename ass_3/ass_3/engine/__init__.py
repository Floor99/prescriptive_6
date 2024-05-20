# from ass_3.maintenance import MaintenanceTime
import pandas as pd
from ass_3.utils import select_engines_for_maintenance


class Engine:
    """
    A class representing an engine.
    
    Attributes:
    - all_engine_costs (list): List of costs associated with each engine based on its ID.
    - all_rul (list): List of Remaining Useful Life (RUL) predictions for all engines.
    """
    
    all_engine_costs = [4 if 1 <= j <= 20 else 3 if 21 <= j <= 30 else 2 if 31 <= j <= 45 else 5 if 46 <= j <= 80 else 6 for j in range(1, 100+1)]
    all_engines = pd.read_csv('ass_3/data/RUL_consultancy_predictions_A3-2.csv', sep = ";")
    all_rul = pd.read_csv('ass_3/data/RUL_consultancy_predictions_A3-2.csv', sep = ";")['RUL'].tolist()
    
    # Read Predictions data with RUL and ids
    prediction_engines = pd.read_csv('ass_3/data/Predictions.csv', sep = ";")
    prediction_rul = pd.read_csv('ass_3/data/Predictions.csv', sep = ";")['RUL'].tolist()
    
    engines_for_maintenance = select_engines_for_maintenance(all_engines, 29)                   # CHANGE TO CORRECT ENGINES
    maintenance_ids = engines_for_maintenance["id"].tolist()
    maintenance_rul = engines_for_maintenance["RUL"].tolist()

    def __init__(self, engine_id:int) -> None:
        """
        Initialize an Engine object.

        Parameters:
        - engine_id (int): The ID of the engine.

        Returns:
        - None
        """
        
        self.engine_id = engine_id
        self.maintenance_rul = self.all_rul[self.engine_id-1]             
        self.get_safety_day()
        self.get_engine_costs()
    
    
    def get_safety_day(self):
        """
        Calculate the safety day for the engine.

        Returns:
        - None
        """

        self.safety_day = 1 + self.maintenance_rul - 1
    
    
    def get_engine_costs(self):
        """
        Retrieve the engine costs based on its ID from the predefined list.

        Returns:
        - None
        """
        
        self.engine_costs = self.all_engine_costs[self.engine_id-1]
        
        
    def __repr__(self) -> str:
        """
        Return a string representation of the Engine object.

        Returns:
        - str: String representation of the Engine object.
        """
        
        class_name = type(self).__name__
        return f"{class_name}(engine_id={self.engine_id!r}, rul={self.maintenance_rul!r})"
    
    


