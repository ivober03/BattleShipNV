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

    def __init__(self, cell, orientation, moves_made):
        """
        Constructor for the Sentence class.
        Initializes the sentence taking into account the ship passed as a parameter, the moves made and it's surrounding cells
        """

        # Initialize an empty set to store the possible target cells
        self.cells = set()

        # Extract the rom and col from the cell
        row, col = cell

        # If it's the first hit:
        if not orientation:

        # Calculate and add the cells immediately surrounding the hit cell as possible targets
            if 0 <= (row - 1) <= 9 and (row - 1, col) not in moves_made:
                self.cells.add((row - 1, col))
            if 0 <= (row + 1) <= 9 and (row + 1, col) not in moves_made:
                self.cells.add((row + 1, col))
            if 0 <= (col - 1) <= 9 and (row, col - 1) not in moves_made:
                self.cells.add((row, col - 1))
            if 0 <= (col + 1) <= 9 and (row, col + 1) not in moves_made:
                self.cells.add((row, col + 1))

        # Else check the orientation and add cells accordingly
        elif orientation == 'vertical':
            if 0 <= (col - 1) <= 9 and (row, col - 1) not in moves_made:
                self.cells.add((row, col - 1))
            if 0 <= (col + 1) <= 9 and (row, col + 1) not in moves_made:
                self.cells.add((row, col + 1))
        else:
            if 0 <= (row - 1) <= 9 and (row - 1, col) not in moves_made:
                self.cells.add((row - 1, col))
            if 0 <= (row + 1) <= 9 and (row + 1, col) not in moves_made:
                self.cells.add((row + 1, col))


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
