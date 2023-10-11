import pygame
import os

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS
PADDING = 5

# RGB   
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)

# Imgs
ruta_imagen = os.path.join("battleship/assets" , "Water.png") 
WATER_IMG = pygame.transform.scale(pygame.image.load(ruta_imagen), (SQUARE_SIZE-10, SQUARE_SIZE-10))