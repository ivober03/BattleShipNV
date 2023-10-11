import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import Board
from battleship.cells import Cell

FPS = 60

# Creates and names a new Window
WIN = pygame.display.set_mode((2*WIDTH, HEIGHT))  
pygame.display.set_caption('Battleship')


# Manages and launches the game loop (if it breaks one of the conditions the loop ends)
def main():

   run = True
   clock = pygame.time.Clock() # Sets the fps to 60
   userboard = Board() # Change to user class later
   enemyboard = Board()

   while run: 
      clock.tick(FPS)
      
      # Catchs all the events made from pygame
      for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
      
      # Draws the board and update the window
      userboard.draw_board(WIN,1)
      enemyboard.draw_board(WIN,2)
      pygame.display.update()

   pygame.quit()

main()