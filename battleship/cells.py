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

    def __init__(self, row:int, col:int, pos):
        """
        Constructor for the Cell class.
        """
        self.pos = pos
        self.row = row
        self.col = col  
              
        # Initialize status to "Hidden" by default,
        self.status = Cell.POSSIBLE_STATUSES[0]
        self.ship = False
        self.pdf_value = 0
        
        self.x = 0
        self.y = 0
        self.calc_pos()



    def make_guess(self, win ):
        """
        Update the cell's status based on a player's guess.
        """
        # If the cell has a part of a ship, update it's status to "Ship"
        if self.ship == True:
            self.status = Cell.POSSIBLE_STATUSES[2]
            self.draw_ship_destroyed(win)
        # Otherwise, set it's status to "Water"
        else:
            self.status = Cell.POSSIBLE_STATUSES[1]
            self.draw_water_cell(win)
            
            
        

    # Used to know where the img is put
    def calc_pos(self):
        if (self.pos == 2):
            self.x = SQUARE_SIZE * self.row +PADDING + (WIDTH + SEPARATION) 
            self.y = SQUARE_SIZE * self.col +PADDING
        else:
            self.x = SQUARE_SIZE * self.row +PADDING
            self.y = SQUARE_SIZE * self.col +PADDING
        
    def set_ship(self):
        self.ship = True
        
    # Draw the cell depending on the needs
    def draw_water_cell(self, win ):
        win.blit(WATER_IMG,(self.x,self.y))

    def draw_ship_cell(self, win ):
        
        win.blit(BLACK_SURFACE,(self.x, self.y))
        win.blit(SHIP_IMG,(self.x, self.y))

    def draw_ship_destroyed(self, win ):
        win.blit(destroyedship.pngxd,(self.x, self.y))
    


          
        

        
        
        
    
        
        
    
