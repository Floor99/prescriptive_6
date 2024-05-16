


class StartDay:
    """
    A class representing the start day of maintenance.

    Methods:
    - __init__(bits:list[int]) -> None: Initialize a StartDay object.
    - decode_bits() -> None: Decode the bit representation of the start day.
    - __repr__() -> str: Return a string representation of the StartDay object.
    """
    
    def __init__(self, bits:list[int]) -> None:
        """
        Initialize a StartDay object.

        Parameters:
        - bits (list[int]): List of bits representing the start day.

        Returns:
        - None
        """
        
        self.bits = bits
        self.decode_bits()
    
    def decode_bits(self) -> None:
        """
        Decode the bit representation of the start day.

        Returns:
        - None
        """
        
        # convert the list of bits into a string representation
        bit_string = "".join(str(bit) for bit in self.bits)
        # convert the binary string representation into an integer
        self.start_day = int(bit_string, 2)
        
    def __repr__(self) -> str:
        """
        Return a string representation of the StartDay object.

        Returns:
        - str: String representation of the StartDay object.
        """
        
        class_name = type(self).__name__
        return f"{class_name}(bits={self.bits!r}, start_day={self.start_day!r})"
    
