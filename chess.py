import board 
import piece 

class Chess():
    """
    Put description of the Chess class here
    """
    def __init__(self):
        # replace `pass` with the desired attributes and add any 
        # additional parameters to the function  
        self.board = board.Board()

    def promotion(self, pos): # not sure what to do with pos ??
        # add any parameters necessary and replace the body with
        # functionality on promoting a Pawn that has reached the 
        # end of the board
        options = ['R','N','B','Q']
        pawn = None

        while pawn == None:
            selection = input("promote pawn to? (R,N,B,Q): ")
            if selection not in options:
                print("Not a valid selection")
            else:
                if selection == "R":
                    pawn = piece.Rook(True)
                if selection == "N":
                    pawn = piece.Knight(True)
                if selection == "B":
                    pawn = piece.Bishop(True)
                if selection == "Q":
                    pawn = piece.Queen(True)
        
        self.board[pos[0]][pos[1]] = pawn # in this case, the promoted pawn!
        

    def move(self):
        # add any parameters necessary and replace the body with
        # functionality of moving a a piece from its current location
        # to a destination
        pass