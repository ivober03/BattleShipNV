"""
Once a ship is hit a new sentence is created using the position of the target. The initial sentence will
have a set() with 4 or fewer potential targets. Later on the ObjectAI class will help narrow down the sentence.
"""

from .ai import *

class Sentence:
    """
    Logical statement about a Battleship game.
    A sentence consists of a set of board cells which are possible targets.
    """

    def __init__(self, cell, orientation, moves_made, ship_limits):
        """
        Constructor for the Sentence class.
        Initializes a sentence taking into account the ship passed as a parameter, the moves made and it's surrounding cells
        """

        # Initialize an empty set to store the possible target cells
        self.cells = set()

        # If a cell is provided extract the row and col
        if cell:
            row, col = cell

        if orientation is not None:
             
            # Ship orientation is known, so add the cells based on ship limits
            min_cell, max_cell = ship_limits

            min_row, min_col = min_cell
            max_row, max_col = max_cell

            if orientation == 'vertical':

                # Extend the range of cells above and below the ship
                if 0 <= (min_col - 1) <= 9 and (min_row, min_col - 1) not in moves_made:
                    self.cells.add((min_row, min_col - 1))
                if 0 <= (max_col + 1) <= 9 and (max_row, max_row +1) not in moves_made:
                    self.cells.add((max_row, max_row +1))

            else:

                # Extend the range of cells to the left and right of the ship
                if 0 <= (min_row - 1) <= 9 and (min_row - 1, min_col) not in moves_made:
                    self.cells.add((min_row - 1, min_col))
                if 0 <= (max_row + 1) <= 9 and (max_row + 1, max_col) not in moves_made:
                    self.cells.add((max_row + 1, max_col))
                    
        else:

            # Orientation is not known, calculate and add the cells surrounding the hit cell
            if 0 <= (row - 1) <= 9 and (row - 1, col) not in moves_made:
                self.cells.add((row - 1, col))
            if 0 <= (row + 1) <= 9 and (row + 1, col) not in moves_made:
                self.cells.add((row + 1, col))
            if 0 <= (col - 1) <= 9 and (row, col - 1) not in moves_made:
                self.cells.add((row, col - 1))
            if 0 <= (col + 1) <= 9 and (row, col + 1) not in moves_made:
                self.cells.add((row, col + 1))


    def add_cell(self, cell):
        """
        Add a new cell to the sentence.
        """

        self.cells.add(cell)


    def remove_cell(self, cell):
        """
        Remove a cell from the sentence.
        """

        self.cells.remove(cell)
