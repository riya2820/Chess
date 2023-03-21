class Board():
    """
    Put description of the Board class here
    # P P P P P P P P
    # R N B Q K B N R
    """
    def __init__(self):
        # replace body with the initialization of a standard
        # chess board with it's pieces placed correctly
        
        self.board = [] # lets make board a 2D list, appending [] in next function 
        self.white_pieces = self.black_pieces = 16 
        self.create_board()

    def create_board(self):
        elements = ['R','N','B','Q','K','B','N','R']
        for row in range(8):
            self.board.append([])
            for col in range(8):
                # see how to put different colors 
                if row < 2: # black pieces 
                    if row == 0:
                        i = 0 
                        while i < 8:
                            self.board[row].append([elements[i]]) 
                            i += 1
                    else:
                        self.board[row].append(['P']*8)

                if row > 5: # white pieces
                    if row == 7:
                        i = 0 
                        while i < 8:
                            self.board[row].append([elements[i]]) 
                            i += 1
                    else:
                        self.board[row].append(['P']*8)


    def print_board(self):
        # replace body with how you want your board printed
        pass