import pygame
from battleship.constants import WIDTH, HEIGHT, SEPARATION, SQUARE_SIZE
from battleship.board import Board
from battleship.cells import Cell
from battleship.user import User
from battleship.ai import OpponentAI
from battleship.game import Game
FPS = 60

# Creates and names a new Window
WIN = pygame.display.set_mode((2*WIDTH + SEPARATION, HEIGHT)) 

pygame.display.set_caption('Battleship')

def get_coords(pos):
   x, y = pos
   row = x // SQUARE_SIZE
   col = y // SQUARE_SIZE
   coords = ((row, col),)
   return coords


# Manages and launches the game loop (if it breaks one of the conditions the loop ends)
def main():

   run = True
   game1 = Game(WIN)
   clock = pygame.time.Clock() # Sets the fps to 60
   
   while run:
      
      clock.tick(FPS)
      game1.Put_boats_stage()
      
      
   pygame.quit()

main()

