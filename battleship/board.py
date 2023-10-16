import pygame

from battleship.cells import Cell
from .constants import *

class Board:

    def __init__(self, pos):
        self.board = []
        self.selected_cell = None 
        self.player_boats_left = self.ia_boats_left = 5
        self.pos = pos
        self.create_board()

        
    # Fills the background with black and draws green lines on the squares
    def draw_squares(self, win):
        
        for row in range(ROWS):
            for col in range(COLS):
                x = 0
                y = 0
                if (self.pos == 2):
                    x = row*(SQUARE_SIZE ) + (WIDTH + SEPARATION) # Used to calc the pos of the second board
                    y = col*(SQUARE_SIZE ) 
                else:
                    x = row*(SQUARE_SIZE)
                    y = col*(SQUARE_SIZE)
                
                pygame.draw.rect(win, GREEN,  (x, y, SQUARE_SIZE, SQUARE_SIZE), 1 )


    # Creates the board internal matrix and fills it with type object cell  

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (self.pos == 2):
                    self.board[row].append(Cell(row, col, self.pos))
                else:
                    self.board[row].append(Cell(row, col, self.pos))

    
    # Iterates over the array and for each cell it draws its content
    
    def get_cell(self, row, col):
        return self.board[row][col]
    
    def draw_board(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.board[row][col]
                cell.draw_water_cell(win)
                
    def draw_ship(self, win, ship):
        for cell in ship.get_cells():
            cell.draw_ship_cell(win)
        
                
    def update_board(self):
        pygame.display.update()
        


    