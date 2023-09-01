class Cell:
    """
    Represents a Cell in the board
    """

    def __init__(self, row, col):
        """
        Constructor for the Cell class.
        Initializes attributes such as row and column.
        """
        self.row = row
        self.col = col
        self.pdf_value = 0


class Ship:
    """
    Represents a ship
    """

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
        if self.turn == "user":
            self.turn = "oponnent"
        else:
            self.turn = "user"


class OpponentAi:
    """
    Represents the AI opponent int he game
    """
    def __init__(self, width, heigth):

        """
        Implement:
        
        Self board
        Oponent board
        
        """
        self.width = width
        self.heigth = heigth
        self.pdf_matrix = [] #Represents the board where the IA makes his guesses
        self.moves_made = set()
        self.mode = "hunt"



    def place_boats_random(self):
        """
        places the boats randomly
        """


    def calculate_pdf(self):
        """
        Calculates the probability density function and adds an euristic value to all the cells 
        """


    def make_guess(self):
        """
        Generates a guess based on sentences and the pdf
        """


    def hunt(self):
        """
        In Hunt mode, fire at random coordinates with even parity to increase chances of hitting ships.
        """


    def target(self):
        """
        In this mode:
        1-Creates a sentence with 4 possible cells to continue hitting the boat
        2-Select from that 4 cells who has the highest euristic value and fires(Iterative till found another part of the ship or sunked)
        3-Creates a new sentence taking into account the orientation and all of the knowledge
        4-Fires at the most probable cell from the sentence 
        5-Iterate 3 and 4 till boat sunked
        """

    
    def update_sentence(self):
        """
        Updates the sentence based on the guess result
        """


class User:
    """
    Represents the human player in the Game
    """
    def __init__ (self, width, heigth, user_ships ):
        
        self.width = width
        self.heigth = heigth
        self.board = []
        self.user_ships = set(Ship)
    

    def place_boats(self):
        """
        Allows the user to place their ships on the board
        """


    def make_move(self):
        """
        Promts the user to make a guess and return the move coordinates
        """    


    def update_user_boardd(self, row, col, result):
        """
        Updates the user's board based on the guess result.
        """



        
        
        
        




        
            