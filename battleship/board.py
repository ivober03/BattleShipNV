import pygame
from .constants import *
class Board:
    def __init__(self):
        self.board = []
        sel.selected_cell = None 
        self.player_boats_left = self.ia_boats_left = 5
        
    # Fills the background with black and draws green lines on the squares
    def draw_cells(self, win):
        win.fill(BLACK)
        
        for row in range(ROWS):
            for col in range(COLS):
                x = row*(SQUARE_SIZE )
                y = col*(SQUARE_SIZE )
                
                pygame.draw.rect(win, GREEN,  (x, y, SQUARE_SIZE, SQUARE_SIZE), 1 )
                
def create_board(self):
    pass
    
