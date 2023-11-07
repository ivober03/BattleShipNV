from battleship.board import *
from battleship.user import *
from battleship.ai import *
import pygame
from battleship.constants import *


WIN = pygame.display.set_mode((2*WIDTH + SEPARATION, HEIGHT)) 

def main():

    Run = True
    clock = pygame.time.Clock() # Sets the fps to 60

    # Create an instance of Board and User to test the AI
    opponent_board = Board(1) 
    opponent = User(opponent_board)
    ai = OpponentAI(None, opponent)
    
    while Run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();

        opponent.put_ship(((6, 7), (6, 8)), WIN) # horizontal size 2 ship
        opponent.put_ship(((1, 3), (2, 3), (3, 3)), WIN) # horizontal size 3 ship
        opponent.put_ship(((5, 6), (5, 7), (5, 8)), WIN) # vertical size 3 ship
        opponent.put_ship(((7, 1), (7, 2), (7, 3), (7, 4)), WIN) # vertical size 4 ship
        opponent.put_ship(((4, 2), (4, 3), (4, 4), (4, 5), (4, 6)), WIN) # vertical size 5 ship
        for i in range(30):
            make_guess_test(ai)

        Run = False

    pygame.quit()


def make_guess_test(ai):
    """
    Tester for make guess method
    """

    knowledge_set = ai.knowledge

    # Simulate a situation where the AI has no knowledge
    if not knowledge_set:
        print("Testing 'make_guess' with no knowledge:")
        is_hit, cell = ai.make_guess()
        print(f"AI's guess: {cell}, Hit: {is_hit}")
        print(f"Knowledge: {knowledge_set}")
        print("-----------------------------------------")

    # Simulate a situation where the AI has no knowledge
    else: 
        print("Testing 'make_guess' with knowledge:")
        is_hit, cell = ai.make_guess()
        knowledge_set = ai.knowledge
        print(f"Knowledge: {knowledge_set}")
        print("-----------------------------------------")

main()
 