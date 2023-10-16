import pygame
from battleship.constants import WIDTH, HEIGHT, SEPARATION, SQUARE_SIZE
from battleship.board import Board
from battleship.cells import Cell
from battleship.user import User

FPS = 60

# Creates and names a new Window
WIN = pygame.display.set_mode((WIDTH + SEPARATION, HEIGHT)) 

pygame.display.set_caption('Battleship')

def get_row_col_from_mouse(pos):
   x, y = pos
   row = y // SQUARE_SIZE
   col = x // SQUARE_SIZE
   return row, col


# Manages and launches the game loop (if it breaks one of the conditions the loop ends)
def main():

   run = True
   clock = pygame.time.Clock() # Sets the fps to 60
   userboard = Board(1) # Change to user class later
   enemyboard = Board(2)
   Player1 = User(userboard)

   while run: 
      clock.tick(FPS)
      
      # Catchs all the events made from pygame
      for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            int.row, int.col = get_row_col_from_mouse(pos)
            Player1.put_ship(((row, col)), WIN)
      
      # Draws the board and update the window
      Player1.get_board().draw_board(WIN)
      enemyboard.draw_board(WIN)
      
      Player1.put_ship(((1,3),(2,3),(3,3),(4,3)), WIN)
      
      pygame.display.update()

   pygame.quit()

main()