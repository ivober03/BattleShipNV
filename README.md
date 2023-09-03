# Introduction:
**Battleship** is a classic 1v1 game, originally played using paper and pencil.

On a grid (usually 10 x 10) players hide ships of different lengths, either up and down or side to side (not diagonally), without any overlaps. For this project, we're using ships of lengths: 5, 4, 3, 3, 2 (which makes 17 possible targets out of the total 100 squares).

### Game rules:

Once both players hide their fleets, they take turns aiming at each other by saying where they want to shoot. When a player shoots, the other says **HIT!** if they hit a ship's part or **MISS!** if it's just water.

The player who sinks the other player's entire fleet (hitting all the spots with ships) wins the game.

# Understanding: 
The AI's strategy will consist of creating a stack of potential targets. Initially, the AI will be in **Hunt** mode, firing at random coordinates (taking into account some heuristic values). Once it hits a ship, the AI switches to **Target** mode. After a hit, the four surrounding grid squares are added to a stack of 'potential' targets.

Cells should only be added to the stack if they have not already been visited.

Once the AI enters in **Target** mode, it shoots at the next potential target from the stack. If it hits again, then a fresh stack of cells will be generated containing new 'potential' targets. The AI leaves the **Target** mode once the ship has been sunk or exhaust the stack.

Note that the AI strategy is dynamic and only considers the most recent set of 'potential' targets. The AI will only take into account the ones generated with the last move. This aproach emulates how a human player might think while playing Battleship.

### Parity: 

Because the smallest ship is at least two units long, we don't need to search every corner of the board randomly. Even the shortest ship needs to cover two neighboring squares.

Think of the board as a checkerboard, like the grid on the left. No matter how we position the two-unit destroyer on the grid, it will always span one white and one black square.

The black squares on the grid have _even parity_, while the white squares have _odd parity_.

We can tell our **Hunt** strategy to only shoot randomly at unknown locations with even parity. Even if we only fire at black locations, we'll manage to hit every ship — there's no way to position a ship without touching at least one blue square.

Once a target is hit and **Target** mode is turned on, the 'parity' rule no longer applies, allowing us to investigate all potential targets. If the algorithm switches back to **Hunt** mode, the parity filter is turned on again.

Once the two-units boat is sunk, we can modify the parity rule for a broader spacing. 

### Probability Density Functions: 

At the start of every new turn, based on the ships still left in the battle, we’ll work out all possible locations that every ship could fit (horizontally or vertically).

Initially, this will be pretty much anywhere, but as more and more shots are fired, some locations become less likely, and some impossible. Every time it’s possible for a ship to be placed in over a grid location, we’ll increment a counter for that cell. The result will be a superposition of probabilities

The concept of PDFs involves determining the likelihood of various events occurring, in this case, the potential positions of enemy ships on the game grid. This approach enables the AI to make informed guesses about the whereabouts of opponent ships and adapt its tactics accordingly.

The PDFs strategy follows the next steps: 

1. **Initialize PDFs for Each Ship:** For each ship size, create a probability matrix that corresponds to the game board. This matrix tracks the likelihood of each cell being occupied by a part of the ship. Initially, all probabilities are equal, reflecting the uncertainty at the start of the game.
    
2. **Update PDFs After Each Turn:** As the game progresses and shots are fired, adjust the probabilities based on the outcomes of each shot. If a cell is hit, its probability drops to zero since a ship part is confirmed. If a cell is a miss, the probability is updated according to the likelihood of a ship occupying the cell.
    
3. **Incorporate Ship Sinks:** When a ship is sunk, update the PDFs to remove the possibility of the ship's presence in relevant cells. This refines the AI's knowledge about the game state.
    
4. **Calculate Most Likely Position:** During the AI's turn, calculate the highest probability cell for each ship size. The cell with the highest probability becomes the target for that ship's shot. This technique focuses the AI's efforts on areas most likely to yield successful hits.
    
5. **Adjust Strategy Based on PDFs:** By leveraging the information from the PDFs, the AI can dynamically adjust its strategy. As the probabilities change with each turn, the AI intelligently adapts its target selection, increasing its chances of hitting opponent ships.


# Specification:
There are two main files in this project: `runner.py` and  `battleship.py`. `battleship.py` contains all of the logic the game itself and for the AI to play as an opponent. `runner.py` contains all of the code to run the graphical interface for the game. 
## battleship.py file:

### 1: **`Cell`** Class:
The `Cell` class represents an individual cell on the game board. Each cell has two coordinates (row, col) and a probability density function (PDF) value, aiding in AI decision-making.

Attributes:

- `row`: The row index of the cell
- `col`: The col index of the cell
- `pdf_value`: A probability density function value for AI decision-making

### 2: **`Ship`** Class:

The `Ship` class represents a ship in the game. It's responsible for storing information about a ship's attributes and state. Each ship has a size (number of cells it occupies), a status (whether it's sunk or not), and the coordinates of its cells on the game board. The class helps manage ships' placement, status, and interactions with the game.

Attributes:

- `health`: The size of the ship (number of cells).
- `cells`: A `set()` containing the coordinates of the cells occupied by the ship.

Methods:

- `place_on_board(self, start_)`: Places the ship on the board by adding its occupied cells to the `cells` set.
- `is_alive(self)`: Checks if the health is greater than 0. Returns true if the ship is still alive, false otherwise.
- `hit(self)`: Handles a hit on the ship by decreasing its health by 1.

### 3: **`Sentence`** Class: 

The `Sentence` class represents a logical sentence that holds information about potential ship placements. Once a ship is hit a new sentence is created using the position of the target. The initial sentence will have a `set()` with 4 or fewer potential targets. As more information becomes available, the `Sentence` objects help narrow down possible positions.

Attributes:

- `cell:` The initial cell that start the new sentence.
- `cells`: A `set()` containing possible cell coordinates where the ship might be located.

Methods:

- `add_cells`: Add cells to the sentence
- `remove_cells`: Remove cells from the sentence

### 4: **`Battleship` Class:** 

The `Battleship` class represents the main game control. The class is responsible for initializing the board, managing player turns, updating game boards, and checking for victory conditions. It creates instances of the `OpponentAI` and `User` classes and coordinates the gameplay.

Attributes:

- `board_width`: The width of the game board.
- `board_height`: The height of the game board.
- `num_boats`: The number of boats in the game.
- `opponent_ai`: An instance of `OpponentAI` class.
- `user`: An instance of `User` class.
- `turn`: A variable indicating whose turn it is (user or opponent).

Methods:

- `check_hit(self, cell)`: Checks if a guess at the specified cell is a hit or miss.
- `switch_turn(self)`: Switches the turn between user and opponent.
- `won(self)`: Returns true if one of  the players have sunk all the enemy boats

### 5: **`OpponentAI` Class:** 

The `OpponentAI` class represents the AI opponent in the game. It's responsible for generating its own game board and placing its ships randomly. The AI makes decisions on where to guess based on available information and strategies. This class interacts with the game through the `Battleship` class to provide a challenging opponent.

The `OpponentAI` class represents the AI opponent in the game.

Attributes:

- `board_width`: The width of the game board.
- `board_height`: The height of the game board.
- `pdf_matrix`: A matrix representing the board. Each cell in this matrix is going to have a pdf value associated to them.
- `moves_made`: A set containing all of the moves made. This set is going to be used in the pdf calculation.
- `mode`: A variable that stores the mode that the AI is in. The AI can be in `hunt` mode or `target`mode.

Methods:

- `place_boats_randomly(self)`: Places boats randomly on the opponent's board.
- `make_guess(self)`: Generates a guess based on logical inferences from sentences and pdf value
- `hunt()`: In **Hunt** mode, fire at random coordinates with even parity to increase chances of hitting ships.  
- `target()`: In **Target** mode, fire at the most probable cell based on PDF matrices. Adjust the mode if a hit occurs or all potential targets are exhausted.
- `calculate_pdf(self)`: Calculates the probability density function for each cell in the pdf_matrix.
- `update_knowledge(self)`: Updates the sentence based on the guess result.
- `generate_sentence(hit)`: Generate a new sentence once a new target is hit

### 6: **`User` Class:** 

The `User` class represents the human player in the game. It's responsible for placing the user's ships on their own board and making guesses on the opponent's board. The class provides methods for user interaction, such as placing ships.

The `User` class represents the human player in the game.

Attributes:

- `board_width`: The width of the game board.
- `board_height`: The height of the game board.
- `user_board`: A 2D list representing the user's game board.
- `user_ships`: A list of `Ship` objects representing the user's ships.

Methods:

- `place_user_boats(self)`: Allows the user to place their ships on the board.
- `make_move(self)`: Prompts the user to make a guess and returns the move coordinates.
- `update_user_board(self, cell, result)`: Updates the user's board based on the guess result.

# Credits
We would like to acknowledge the following resources that contributed to the development of this game:

- http://www.datagenetics.com/blog/december32011/: This blog provides an analysis of the game and insightful strategies that influenced the AI opponent's behavior.

- CS50AI Course: The game design and logic were inspired by concepts learned in the CS50AI course, which provided a foundation for creating intelligent opponents and game mechanics.

- OpenAI: The development of this game was facilitated by the use of OpenAI's GPT-3.5 language model, which provided valuable assistance and guidance throughout the design and implementation process.

