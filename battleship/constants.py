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

BOATH5 =  [ pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatH" , "5Boat(1).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatH" , "5Boat(2).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatH" , "5Boat(3).png")), 
           pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatH" , "5Boat(4).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatH" , "5Boat(5).png"))]

BOATV5 = [ pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatV" , "5BoatV(5).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatV" , "5BoatV(4).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatV" , "5BoatV(3).png")), 
           pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatV" , "5BoatV(2).png")), pygame.image.load(os.path.join("battleship/assets/5Boat/5BoatV" , "5BoatV(1).png"))]