"""
A ship type object will be created during the ship positioning stage managed from the main.
When said ship is located, the constructor will be called to initialize the corresponding ship.

The main function will be responsible for guaranteeing the correct positioning of all the ships,
this includes overlaping, number of cells occupied by each ship and number of ships.
"""

class Ship:
    """
    Represents a ship object in the game.
    """

    def  __init__(self, cells):
        """
        Constructor for the Ship class.
        """

        self.cells = cells
        self.hitted_cells = set()
        self.size = len(cells)
        self.health = self.size


    def is_alive(self):
        """
        Returns True if the ship is alive (health > 0), returns False otherwise.
        """

        return self.health > 0


    def hit(self, coord):
        """
        Decreases ship's health by 1 and stores the hitted cell.
        """

        if self.health != 0:
            self.health -= 1
            self.hitted_cells.add(coord)


    def is_a_hitted_cell(self, coord):
        """
        Returns True if the coordinates passed as a parameter is in hitted_cells, returns False otherwise
        """

        return coord in self.hitted_cells
        
