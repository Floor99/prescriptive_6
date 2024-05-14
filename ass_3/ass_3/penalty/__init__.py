from ass_3.day import StartDay
from ass_3.engine import Engine


class EnginePenalty:
    def __init__(self, start_day:StartDay, engine:Engine) -> None:
        """
        Initialize a Penalty object.

        Parameters:
        - start_day (StartDay): The start day of the maintenance.
        - engine (Engine): The engine associated with the penalty.

        Returns:
        - None
        """
        
        self.start_day = start_day
        self.engine = engine
        self.get_penalty()

    
    def get_penalty(self):
        """
        Calculate the penalty of an engine when the safety date is overdue.

        Returns:
        - None
        """
        
        days_beyond_safety_day = self.start_day.start_day - self.engine.safety_day
        
        if days_beyond_safety_day < 0:
            days_beyond_safety_day = 0
        
        self.penalty = self.engine.engine_costs * days_beyond_safety_day**2
        
        if self.penalty > 250:
            self.penalty = 250
    
        
           
    def __repr__(self) -> str:
        """
        Return a string representation of the Penalty object.

        Returns:
        - str: String representation of the Penalty object.
        """
        
        class_name = type(self).__name__
        return f"{class_name}(day_after_safety_day={self.start_day!r}, engine={self.engine!r}, penalty={self.penalty!r})"
    
    
