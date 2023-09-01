import random


class Cell:

    def __init__(self, row, col):
        """
        Constructor for the Cell class.
        Initializes attributes such as row and column.
        """
        self.row = row
        self.col = col
        self.pdf_value = 0


class Ship:

    def __init__(self, size):
        """
        Constructor for the Ship class.
        Initializes attributes such as health and cells.
        """
        self.health = size  # Initialize health based on ship size
        self.cells = []  # Keep track of occupied cells on the board

    def place_on_board(self, cells):
        """
        Places the ship on the board and updates the occupied cells list.
        """
        self.cells = cells

    def is_alive(self):
        """
        Checks if the ship is still afloat (health > 0).
        Returns True if the ship is alive, False otherwise.
        """
        return self.health > 0

    def hit(self):
        """
        Handles a hit on the ship, decreasing health by 1.
        """
        self.health -= 1


class Sentence:
    """
    Logical statement about a Battleship game.
    A sentence consists of a set of board cells which are possible targets.
    """

    def __init__(self, ship, cells):
        """
        Constructor for the Sentence class.
        Initializes the ship and its corresponding cells.
        """

    def __eq__(self, other):
        """
        Compare sentences.
        """

    def __str__(self):
        """
        Sentence as a string.
        """

    def add_cells(self, cells):
        """
        Add cells to the sentence.
        """

    def remove_cells(self, cells):
        """
        Remove cells from the sentence.
        """

class Battleship:
    """
    Battleship game representation
    """

    def __init__(self, width=10, heigth=10):
        """
        Implement:
        User:create a instance of user class
        OponnentIA: create a instance of OponentIA class
        
        
        """
        self.width = width
        self.heigth = heigth
        self.board = [] #remember to intialize the matrix board
        self.turn = "user"
        
    def won(self):
        """
        Indicates if one of the players haves sunked all the enemy boats
        """

    def check_hit(self, cell):
        """
        Indicates if the guess at the specified cell is a hit or a miss
        """
        self.cell = cell

    def switch_turn(self):
        """
        Switches the turn beetwen user and opponent
        """
        if(self.turn == "user"):
            self.turn = "oponnent"
        else:
            self.turn = "user"
            self.caca=2

        
        




        
            