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
        Returns the sentence as a string.
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
        Constructor for the battleship class.
        Initializes the board, user, and opponent.
        """
        self.width = width
        self.heigth = heigth
        self.board = [] # remember to intialize the matrix board
        self.turn = "user"
        
        
    def won(self):
        """
        Returns true if one of the players haves sunked all the enemy boats
        """


    def check_hit(self, cell):
        """
        Returns true if the shot at the specified cell is a hit, otherwise returns false
        """


    def switch_turn(self):
        """
        Switches the turn beetwen the players
        """
        if self.turn == "user":
            self.turn = "oponnent"
        else:
            self.turn = "user"


class OpponentAi:
    """
    Represents the AI opponent
    """

    def __init__(self, width, heigth):
        """
        Constructor for the AI opponent.
        """
        self.width = width
        self.heigth = heigth
        self.pdf_matrix = [] # 
        self.moves_made = set()
        self.mode = "hunt"


    def place_boats_random(self):
        """
        Places AI boats randomly
        """


    def calculate_pdf(self):
        """
        Calculates the probability density function and adds an euristic value to all the cells 
        """


    def make_guess(self):
        """
        Makes a guess based on sentences and the pdf value for each cell
        """


    def hunt(self):
        """
        In Hunt mode, fire at random coordinates with even parity.
        """


    def target(self):
        """
        Enter target mode once a boat is hit, then:
            1-Create a sentence with 4 possible cells to continue hitting the boat.
            2-Select from that 4 cells who has the highest euristic value and fire.
            3-Create a new sentence taking into account the orientation and all available knowledge.
            4-Fire at the most probable cell from the sentence.
            5-Iterate steps 3 and 4 till the boat is sunked or no new sentence can be generated.
        """

    
    def update_knowledge(self):
        """
        Updates the sentence based on the guess result(hit or miss)
        """

    def generate_sentence(self):
        """
        Generate a new sentence once a target is hitn
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



        
        
        
        




        
            