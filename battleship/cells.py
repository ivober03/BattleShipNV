from .constants import *

class Cells:
    def __init__(self, row:int, col:int):
        self.row = row 
        self.col = col 
        self.status = "Hidden"
        self.boat = False
        self.pdf_value = 0
        
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.calc_pos()
        
    def calc_pos(self):
        self.sx = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        self.sy = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.ex = SQUARE_SIZE * self.row
        self.ey = SQUARE_SIZE * self.col
        
        
        
    def set_boat(self):
        self.boat = True
            
        
    def guess(self):
        if (self.status == "Hidden boat"):
            status = "boat"
        if(self.status == "Hidden"):
            status = "water"
            
    def draw_water(self, win ):
        pygame.draw.aaline(win, GREEN, (self.sx, self.sy),(self.ex, self.ey), 1 )
        
            

        
        
        
    
        
        
    