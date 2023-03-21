from ipaddress import collapse_addresses
from sqlite3 import Row
# maybe?
# import board 

# make functions to check validity of moves
# such as check diagonal etc etc

class Piece():
    """
    Put description of the Piece class here
    """
    def __init__(self, name, color):
        # add any additional parameters
        # standard initiation of a piece 
        self.name = ""
        self.color = color
        
    def is_valid_move(self):
        return False

    def is_white(self):
        return self.color == 'WHITE'

    def __str__(self):
        # replace the body and return a string with how you want your piece
        # to be printed as when `print([A Piece Object])` is called
        # return str(self.piece)
        return ''
        
# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation
class Rook(Piece):
    def __init__(self, color):
        # super().__init__(...) can be super helpful in just calling the 
        # parrent init function to avoid the same lines of code
        super().__init__(color)
        self.name = "R"

    def is_valid_move(self, board, start, to):
        '''
        if self.board[start][to] == "":
            # move piece here   
        '''    
        pass

class Knight(Piece):
    def __init__(self):
        self.name = "N"

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self):
        self.name = "B"

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self):
        self.name = "Q"

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self):
        self.name = "K"

    def is_valid_move(self):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        self.name = "P"

    def is_valid_move(self):
        pass