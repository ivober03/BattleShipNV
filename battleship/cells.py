from .constants import *

class Cell:
    def __init__(self, row:int, col:int):
        self.row = row 
        self.col = col 
        self.status = "Hidden"
        self.boat = False
        self.pdf_value = 0
        
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.row  
        self.y = SQUARE_SIZE * self.col 
      
        
        
        
    def set_boat(self):
        self.boat = True
            
        
    def guess(self):
        if (self.status == "Hidden boat"):
            status = "boat"
        if(self.status == "Hidden"):
            status = "water"
            
    def draw_water(self, win ):
        win.blit(WATER_IMG,(x,y))
        
            

        
        
        
    
        
        
    