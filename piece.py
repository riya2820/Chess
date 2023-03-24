import board 

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
        self.board = board.Board()
        
    def is_valid_move(self):
        return False

    def is_white(self):
        return self.color == 'WHITE'

    def __repr__(self):
        return f"{self.color} {self.__class__.__name__}"
        
# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation
class Rook(Piece):
    def __init__(self, color):
        # super().__init__(...) can be super helpful in just calling the 
        # parrent init function to avoid the same lines of code
        super().__init__(color)
        self.name = "R"

    def is_valid_move(self, board, start, end):
        '''
        if self.board[start][to] == "":
            # move piece here   
        '''    
        pass

class Knight(Piece):
    def __init__(self):
        self.name = "N"

    def is_valid_move(self, board, start, end):
        pass

class Bishop(Piece):
    def __init__(self):
        self.name = "B"

    def is_valid_move(self, board, start, end):
        pass

class Queen(Piece):
    def __init__(self):
        self.name = "Q"

    def is_valid_move(self, board, start, end):
        pass

class King(Piece):
    def __init__(self):
        self.name = "K"

    def is_valid_move(self, board, start, end):
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

    def is_valid_move(self, board, start, end):
        return False

class Pawn(Piece):
    def __init__(self):
        # super().__init__()
        self.name = "P" 

    def is_valid_move(self, board, start, end):
        # can move: up (x, y+1) 
        # capture: left (x-1, y) & right (x+1,y)
        x0, y0 = start//8, start%8
        x1, y1 = end//8, end%8

        if (x0, y0+1) == (x1, y1) and self.board[x1][y1] == "-":
            return True # is valid
        # how to check if prev piece was "p" or "P" ??!!
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "P" and self.board[x0][y0] == "p":
            return True
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "p" and self.board[x0][y0] == "P":
            return True
        #else:
        #   print("move is not valid!")
        #     raise Error
        return False
