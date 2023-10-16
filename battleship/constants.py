import pygame
import os

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS
PADDING = 5
SEPARATION = 10

# RGB   
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)

# Imgs
BLACK_SURFACE = pygame.Surface((SQUARE_SIZE-10, SQUARE_SIZE-10))
WATER_IMG = pygame.transform.scale(pygame.image.load(os.path.join("battleship/assets" , "Water.png") ), (SQUARE_SIZE-10, SQUARE_SIZE-10))
SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("battleship/assets" , "Ship.png") ), (SQUARE_SIZE-10, SQUARE_SIZE-10))