

class Team:
    def __init__(self, bits:list[int]) -> None:
        """
        Initialize a Team object.

        Parameters:
        - bits (list[int]): List of bits representing the team.

        Returns:
        - None
        """
        self.bits = bits
        self.decode_bits()
        
    def decode_bits(self) -> None:
        """
        Decode the bit representation of the team.

        This method converts the list of bits into an integer and determines the
        team type ('a' or 'b') based on the decoded integer.
        
        Returns:
        - None
        """
        bit_string = "".join(str(bit) for bit in self.bits)
        self.team = int(bit_string,2)
        self.kind = "a" if self.team == 0 or self.team == 2 else "b"
        
    def __repr__(self) -> str:
        """
        Return a string representation of the Team object.

        Returns:
        - str: String representation of the Team object.
        """
        class_name = type(self).__name__
        return f"{class_name}(bits={self.bits!r}, team={self.team!r}, kind={self.kind!r})"
    

