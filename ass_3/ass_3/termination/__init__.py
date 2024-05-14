from abc import ABC, abstractmethod
import time


class Termination(ABC):
    """
    Abstract base class representing termination criteria for an algorithm.

    Methods:
    - meets_termination(): Abstract method for checking if termination criteria are met.

    Returns:
    - bool: True if termination criteria are met, False otherwise.
    """
    
    @abstractmethod
    def meets_termination(self):
        """
        Abstract method for checking if termination criteria are met.

        Returns:
        - bool: True if termination criteria are met, False otherwise.
        """
        
        pass
    

class TimeTermination(Termination):
    def __init__(self, max_duration:float) -> None:
        """
        Initialize a TimeTermination object.

        Parameters:
        - max_duration (float): The maximum duration for the algorithm to run.

        Returns:
        - None
        """
        
        self.max_duration = max_duration


    def meets_termination(self, start_time:float):
        """
        Check if termination criteria based on time are met.

        Parameters:
        - start_time (float): The start time of the algorithm.

        Returns:
        - bool: True if termination criteria are met, False otherwise.
        """
        
        if time.time() - start_time >= self.max_duration:
            return True
        return False

