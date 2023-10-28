from .constants import *
from .ship import *

class User:
    
    def __init__ (self, board):
        self.board = board
        self.ships = []
        
          
    def get_board(self):
        return self.board
    

    def get_ship(self, cell):
        """
        Given a cell, return the ship that contains it
        """
        
        for ship in self.ships:

            ship_set = set()
            cells = ship.get_cells()

            for ship_cell in cells:
                ship_set.add(ship_cell.get_cell())

            if cell in ship_set:
                return ship
            
        return None  # Return None if the cell is not part of any ship


    def ask_if_hit(self, row, col):
        """
        Returns True if the cell passed as a parameter contains a ship.
        Decreases ship's life by one.
        """     
        hit = self.board.get_cell(row, col).is_ship()
        if hit:
           self.get_ship((row, col)).hit((row, col))

        return hit


    def ask_if_sunken(self, cell):
        """
        Given a ship, return True if sunken. False otherwise.
        """ 
        ship = self.get_ship(cell)
        return ship.sunken()

    
    def put_ship(self, coords, win):
        # Todo: manjear poner el barco y obtener las celdas a partir de la primera celda y la orientacion
        """ This is the principal method to put the ships and manages all of the classes similar methods"""
        temp_cells = []
        # coords = set of tuples with the rows and cols of the selected cells to be ships 
        for (row, col) in coords:
           temp_cells.append(self.board.get_cell(row, col))
        
        ship = Ship(temp_cells) #Creates the ship
        self.board.draw_ship(win, ship) # draws it in the user board
        self.ships.append(ship) #Stores all the user ships 
       
        return ship
    

        
        
        
    