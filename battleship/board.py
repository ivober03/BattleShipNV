import pygame

from battleship.cells import Cell
from .constants import *
class Board:
    def __init__(self):
        self.board = []
        self.selected_cell = None 
        self.player_boats_left = self.ia_boats_left = 5
        self.create_board()
        
    # Fills the background with black and draws green lines on the squares
    def draw_squares(self, win):
        win.fill(BLACK)
        
        for row in range(ROWS):
            for col in range(COLS):
                x = row*(SQUARE_SIZE )
                y = col*(SQUARE_SIZE )
                
                pygame.draw.rect(win, GREEN,  (x, y, SQUARE_SIZE, SQUARE_SIZE), 1 )
                
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Cell(row,col))
    
    def draw_board(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                cell =self.board[row][col]
                if cell != 0:
                    cell.draw_water_cell(win)