from .constants import *

"""
The Battleship field will be represented as a cell board. Every cell on the board will be an instance of the Cell class.
When playing, the User and the AI will try to guess where the ships are, that is, they will make their guesses in a cell on the board.

The cell class must provide methods to determine if said guess touched a ship or water.
At the same time, it must graphically update the cell to represent said result.

At the beginning of the game each cell will be hidden. As the user and the AI make their guesses the cells will update their status to: Water or Ship.
Note that when the User and AI place their ships, this will be represented in the ship's attribute as True. But the status will remain Hidden until that cell is hited.
"""

class Cell:
    """
    Represents a cell object in the board.
    """

    # Define a class-level variable to hold possible status values
    POSSIBLE_STATUSES = ["Hidden", "Water", "Ship"]

    def __init__(self, row:int, col:int):
        """
        Constructor for the Cell class.
        """

        self.row = row
        self.col = col
        # Initialize status to "Hidden" by default,
        self.status = cell.POSSIBLE_STATUSES[0]
        self.ship = False
        self.pdf_value = 0

        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.calc_pos()


    def set_boat(self):
        self.boat = True


    def make_guess(self):
        """
         Update the cell's status based on a player's guess.
        """

        # If the cell has a part of a ship, update it's status to "Ship"
        if self.ship:
            self.status = Cell.POSSIBLE_STATUSES[2]
        # Otherwise, set it's status to "Water"
        elif:
            self.status = Cell.POSSIBLE_STATUSES[1]


    def calc_pos(self):
        self.sx = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        self.sy = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.ex = SQUARE_SIZE * self.row
        self.ey = SQUARE_SIZE * self.col


    def draw_water_cell(self, win ):
        pygame.draw.aaline(win, GREEN, (self.sx, self.sy),(self.ex, self.ey), 1 )

        
        
        
    
        
        
    
