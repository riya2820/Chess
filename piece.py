#from ipaddress import collapse_addresses
# from msilib.schema import Error
# from sqlite3 import Row
# maybe?
from fcntl import F_SEAL_SEAL
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
        r0, c0 = ord(start[0].lower())-ord("a"), start[1]
        r1, c1 = ord(end[0].lower())-ord("a"), end[1]

        if r0 != r1 and c0 != c1:
            return False # rook piece has to be in either same row or col 
        
        if r0 == r1: # moving in the same row
            col_range = range(min(c0,c1)+1, max(c0,c1))
            for col in col_range:
                if self.board[r1][col] != "-":
                    return False # Path blocked 
                return True  

        if c0 == c1: # moving in the same row
            row_range = range(min(r0,r1)+1, max(r,r1))
            for row in row_range:
                if self.board[row][c1] != "-":
                    return False # Path blocked 
                return True  

        return False 
                
        '''
        else: # that means in the same col

        if (x0, y0+1) == (x1, y1) and self.board[x1][y1] == "-":
            return True # is valid
        # how to check if prev piece was "p" or "P" ??!!
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "P" and self.board[x0][y0] == "p":
            return True
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "p" and self.board[x0][y0] == "P":
            return True '''
            
        return False


class Knight(Piece):
    def __init__(self):
        self.name = "N"

    def is_valid_move(self, board, start, end):
        r0, c0 = ord(start[0].lower())-ord("a"), start[1]
        r1, c1 = ord(end[0].lower())-ord("a"), end[1]

        if r0 == r1 and c0 == c1: # not valid
            return False 
        
        # + 2 direction (u,d,l,r) +1 (u,d,l,r)
        row_distance = abs(r1-r0)
        col_distance = abs(c1-c0) 

        # don't need to check path in this case, as knights can hop over pieces!
        if (row_distance == 2 and col_distance == 1) or (col_distance == 2 and row_distance == 1):
            return True

        return False 

class Bishop(Piece):
    def __init__(self):
        self.name = "B"

    def is_valid_move(self, board, start, end):
        r0, c0 = ord(start[0].lower())-ord("a"), start[1]
        r1, c1 = ord(end[0].lower())-ord("a"), end[1]

        if r0 == r1 and c0 == c1 or r0 == r1 or c0 == c1: # not valid
            return False 
        
        row_direction = 1 if r1 > r0 else -1
        col_direction = 1 if c1 > c0 else -1
     
        row, col = r0+row_direction, c0+col_direction 
        while row != r1 and col != c1: # havent reached yet! checking path
            if self.board[row][col] != "-":
                return False # path blocked 
            row += row_direction
            col += col_direction

        return True 


            

class Queen(Piece):
    def __init__(self):
        self.name = "Q"

    def is_valid_move(self, board, start, end):
        r0, c0 = ord(start[0].lower())-ord("a"), start[1]
        r1, c1 = ord(end[0].lower())-ord("a"), end[1]

        row_direction = 1 if r1>r0 else -1
        col_direction = 1 if r1>r0 else -1

        
        if r0 == r1: # moving in the same row
            col_range = range(min(c0,c1)+1, max(c0,c1))
            for col in col_range:
                if self.board[r1][col] != "-":
                    return False # Path blocked 
                return True  

        if c0 == c1: # moving in the same row
            row_range = range(min(r0,r1)+1, max(r,r1))
            for row in row_range:
                if self.board[row][c1] != "-":
                    return False # Path blocked 
                return True  

        if r0 != r1 and c0 != c1: # moving like  a bishop  
            row, col = r0+row_direction, c0+col_direction 
            while row != r1 and col != c1: # havent reached yet! checking path
                if self.board[row][col] != "-":
                    return False # path blocked 
                row += row_direction
                col += col_direction
            

        return True

class King(Piece):
    def __init__(self):
        self.name = "K"
        self.king_moved = False

    def is_valid_move(self, board, start, end):
        r0, c0 = ord(start[0].lower())-ord("a"), start[1]
        r1, c1 = ord(end[0].lower())-ord("a"), end[1]

        # possible moves
        if (r1 == r0+1 and c1 == c0) or (c1 == c0+1 and r0 == r1) or (r1 == r0-1 and c1 == c0) or (r1 == r0 and c1 == c0-1) and r1 >=0 and c1 >= 0:
            self.king_moved = True
            return True

        return False

    
    # I added an extra method for the King class
    def can_castle(self, start, end):
        # if king has moved --> False 
        if self.king_moved:
            return False
        # if rook has moved --> False
        if self.board[start].has_moved:
            return False

        else:
            # can move if 
            # 1) king not under check 
            if start[0] < self.position[0]:
                direction  = -1 # left
            else:
                direction = 1 # right

            # 2) no pieces between king and rook 
            current_col = self.position[1] + direction 
            while current_col != start[1]:
                if self.board[(self.position[0], current_col)] != "-":
                    return False
                current_col += direction # update the col number
            
            # 3) new position should not be in check 
            if self.board.is_square_under_attack(self.position, self.color) or self.board.is_square_under_attack(end, self.color):
                return False

            return True # all clear, can castle

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
        x0, y0 = ord(start[0].lower())-ord("a"), start[1]
        x1, y1 = ord(end[0].lower())-ord("a"), end[1]

        if (x0, y0+1) == (x1, y1) and self.board[x1][y1] == "-":
            return True # is valid
        # how to check if prev piece was "p" or "P" ??!!
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "P" and self.board[x0][y0] == "p":
            return True
        if ((x0-1, y0) == (x1, y1) or (x0+1, y0) == (x1, y1)) and self.board[x1][y1] == "p" and self.board[x0][y0] == "P":
            return True

        return False


        return False

