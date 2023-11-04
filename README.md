# BattleShipNV 

## Description: 

**BattleShipNV** is an implementation of the classic Battleship game. Featuring an intelligent AI opponent, this project delivers a strategic gaming experience with a unique aesthetic and an original soundtrack, setting it apart from the traditional Battleship game. 

### Walk-through video:

### Screenshots: 

*completar*


## AI Methodology

The AI opponent employs a strategy that combines two modes: **Hunt** and **Target**. 

### Hunt Mode

The AI begins in **Hunt** mode, where it randomly selects coordinates to fire at. This random selection is not entirely arbitrary; it's guided by heuristics that help the AI make informed choices. This mode continues until the AI successfully hits an enemy ship.

### Target Mode

After a successful hit, the AI switches to **Target** mode. In this mode, the AI's objective is to systematically eliminate the enemy ship it initially hit.

#### Target Selection

In **Target** mode, the AI maintains a stack of 'potential' target cells. At first these potential target cells are determined based on the cells surrounding the initial hit. The AI prioritizes these cells based on their heuristic values.

The AI selects the cell from the stack with the highest heuristic value as its next target. 

#### Ship Orientation

Once the AI makes another hit, it gains knowledge about the orientation of the enemy ship. Specifically, it can determine whether the ship is placed horizontally or vertically.

#### Target Refinement

With knowledge of the ship's orientation, the AI updates its stack of potential targets to only include cells that match the determined orientation.

#### Backup Stack

To prepare for situations where the first two hit cells may not belong to the same ship, the AI maintains a backup stack of the original potential cells.

### AI Optimization: 

### Parity: 

Because the smallest ship is at least two units long, we don't need to search every corner of the board randomly. Even the shortest ship needs to cover two neighboring squares.

Think of the board as a checkerboard, like the grid on the left. No matter how we position the two-unit destroyer on the grid, it will always span one white and one black square.

The black squares on the grid have _even parity_, while the white squares have _odd parity_.

We can tell our **Hunt** strategy to only shoot randomly at unknown locations with even parity. Even if we only fire at black locations, we'll manage to hit every ship — there's no way to position a ship without touching at least one blue square.

Once a target is hit and **Target** mode is turned on, the 'parity' rule no longer applies, allowing us to investigate all potential targets. If the algorithm switches back to **Hunt** mode, the parity filter is turned on again.

Once the two-units boat is sunk, we can modify the parity rule for a broader spacing. 

### Probability Density Functions: 

At the start of every new turn, based on the ships st is responsible for generating its own game board and placing its ships randomly.ill left in the battle, we’ll work out all possible locations that every ship could fit (horizontally or vertically).

Initially, this will be pretty much anywhere, but as more and more shots are fired, some locations become less likely, and some impossible. Every time it’s possible for a ship to be placed in over a grid location, we’ll increment a counter for that cell. The result will be a superposition of probabilities

The concept of PDFs involves determining the likelihood of various events occurring, in this case, the potential positions of enemy ships on the game grid. This approach enables the AI to make informed guesses about the whereabouts of opponent ships and adapt its tactics accordingly.


## Specification:

*completar*

# How to run:

*completar*

## Credits

We would like to acknowledge the following resources that contributed to the development of this game:

- [DataGenetics Blog](http://www.datagenetics.com/blog/december32011/):This blog provides an analysis of the game and insightful strategies that influenced the AI opponent's behavior.

- [Cliam Brown's Battleship Methodology](https://cliambrown.com/battleship/methodology.php): This resource provided an in-depth perspective on calculating heuristic values for the Battleship game.

- CS50AI Course: The game design and logic were inspired by concepts learned in the CS50AI course, which provided a foundation for creating intelligent opponents and game mechanics.

- OpenAI: The development of this game was facilitated by the use of OpenAI's GPT-3.5 language model.
