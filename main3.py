import pygame
from battleship.constants import WIDTH, HEIGHT, SEPARATION, SQUARE_SIZE
from battleship.board import Board
from battleship.cells import Cell
from battleship.user import User
from battleship.ai import Ai

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
   clock = pygame.time.Clock() # Sets the fps to 60
   userboard = Board(1) # Change to user class later
   enemyboard = Board(2)
   Player1 = User(userboard)
   enemy = Ai(enemyboard)
   vueltas = 0
   while run:
      vueltas = 1+vueltas
      clock.tick(FPS)
      
      # Catchs all the events made from pygame
      for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            coords = get_coords(pos)
            for (row, col) in coords:
               if (row < 10 and col<10):
                  print (coords)
                  Player1.put_ship(coords, WIN)
                  pygame.display.update()
      
      # Draws the board and update the window
      if vueltas == 1:
         Player1.get_board().draw_board(WIN)
         enemy.get_board().draw_board(WIN)
         enemy.place_ship(WIN, 4)
         enemy.place_ship(WIN, 2)
         enemy.place_ship(WIN, 5)
         enemy.place_ship(WIN, 3)
         
         Player1.put_ship(((1,3),(2,3),(3,3),(4,3), (5,3)), WIN)
         
         pygame.display.update()

   pygame.quit()

main()

