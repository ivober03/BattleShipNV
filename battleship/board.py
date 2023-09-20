import pygame
from .constants import *
class Board:
    def __init__(self):
        self.board = []
        self.selected_guess = None
        self.player_boats_left = self.ia_boats_left = 5
        self.status = "Water"

    def draw_cells(self, win):
        win.fill(BLACK)
        
        for row in range(ROWS):
            for col in range(COLS):
                x = row*(SQUARE_SIZE )
                y = col*(SQUARE_SIZE )
                
                pygame.draw.rect(win, GREEN,  (x, y, SQUARE_SIZE, SQUARE_SIZE), 1 )
    
