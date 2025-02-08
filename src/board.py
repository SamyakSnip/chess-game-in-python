from const import *
from square import Square

class Board:
    
    def __init__(self):
        self.squars = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)] #! a list of 8 colums is formed
        
        self._create()
    
    def _create(self):
        print(self.squars)
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squars[row][col] = Square(row, col) 
    
    def _add_pieces(self, color):
        pass

b = Board()
b._create()