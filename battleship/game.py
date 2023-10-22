import pygame
from .board import Board
from .cells import Cell
from .user import User
from .ai import OpponentAI
from .constants import *

class Game: 
    
    def __init__(self, win):
        self.state = "Put_boats_stage"
        self.Player1 = User(Board(1))
        self.enemy = OpponentAI(Board(2), self.Player1)
        
        self.win = win
        self.vueltas = 0
        self.turn = "Player"
        
    def Put_boats_stage(self):
        self.vueltas = self.vueltas+1
        # Catchs all the events made from pygame
        for event in pygame.event.get():

            if event.type ==pygame.QUIT:
                pygame.quit();

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                coords = self.get_coords(pos)
                for (row, col) in coords:
                    if (row < 10 and col<10):
                        print (coords)
                        self.Player1.put_ship(coords, self.win)
                        pygame.display.update()

            if event.type == pygame.BUTTON_MIDDLE:
                event.button == 1
                self.flip_boat()
      
            # Draws the board and update the window
        if (self.vueltas == 1):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS )
            self.Player1.get_board().draw_board(self.win)
            self.enemy.get_board().draw_board(self.win)
            self.enemy.place_ship(self.win, 5)
            
                    
            pygame.display.update()
    
    def flip_boat(self):
        # Todo: a class to manage a window with boats to select and put on the board, they change acording to the orientation
        pass
    
    def state_manager(self):     
        if (self.state == 'Put_boats_stage'):
            self.Put_boats_stage()
        
        
        
    def get_coords(self, pos):
        x, y = pos
        row = x // SQUARE_SIZE
        col = y // SQUARE_SIZE
        coords = ((row, col),)
        return coords

    def update(self):
        player.get_board().draw_board(self.win)
        enemy.get_board().draw_board(self.win)