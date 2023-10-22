class Placeholder:
    
    def __init__(self, size, win):
        self.size = size
        self.win = win
        
    def draw_placeholder(self):
        self.win.blit(PLACEHOLDER4,1,1)
    
           