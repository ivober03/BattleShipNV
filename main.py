

print ("hello")

class Ship:

    """"Class representing a ship of difrent size and position"""

    def __init__(self, size):
        """
        Include:
        Health
        cells: set of coordenates of the boat in the board
        """
        raise NotImplementedError

    def place_on_board(self, cells ):
        """
        Places the ship on the board, and stores the cells ocupied by the boat
        """
        raise NotImplementedError
    
    def is_alive(self):
        """
        Returns true if the boat haves at least 1 of health
        """
        raise NotImplementedError
    
    def hit(self):
        """
        Decrements the health by 1
        """
        raise NotImplementedError
    



