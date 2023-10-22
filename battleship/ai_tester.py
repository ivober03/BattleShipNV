from .board import *
from .user import *
from .ai import *
import pygame
from .constants import *

class AITester:

    WIN = pygame.display.set_mode((2*WIDTH + SEPARATION, HEIGHT)) 

    def __init__(self):
        
        # Create an instance of Board and User to test the AI
        opponent_board = Board(1)        
        opponent_board.create_board()

        self.opponent = User(opponent_board)
        self.opponent.put_ship(((1, 3), (2, 3), (3, 3), (4, 3), (5, 3)), WIN)
        self.opponent.put_ship(((4, 7), (5, 7), (6, 7), (7, 7), (8, 7)), WIN)
       
        # Create an instance of OpponentAI
        self.ai = OpponentAI(None, self.opponent)
        

    def make_guess_test(self):
        """
        Tester for make guess method
        """
        knowledge_set = self.ai.knowledge
        # Simulate a situation where the AI has no knowledge
        if not knowledge_set:
            print("Testing 'make_guess' with no knowledge:")
            is_hit, cell = self.ai.make_guess()
            print(f"AI's guess: {cell}, Hit: {is_hit}")
            print(f"Knowledge: {knowledge_set}")
        else: 
            print("Testing 'make_guess' with knowledge:")
            is_hit, cell = self.ai.make_guess()
            print(f"AI's guess: {cell}, Hit: {is_hit}")
            print(f"Knowledge: {knowledge_set}")


