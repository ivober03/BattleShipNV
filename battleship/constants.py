import pygame
import os

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

# RGB   
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)

# Imgs
ruta_imagen = os.path.join("battleship" , "Water.png")
WATER_IMG = pygame.image.load(ruta_imagen)
WATER_IMG = pygame.transform.scale(WATER_IMG, (SQUARE_SIZE, SQUARE_SIZE))