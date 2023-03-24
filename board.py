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
        self.symbols = {
            'P': '♙',
            'R': '♖',
            'N': '♘',
            'B': '♗',
            'Q': '♕',
            'K': '♔',
            'p': '♟',
            'r': '♜',
            'n': '♞',
            'b': '♝',
            'q': '♛',
            'k': '♚',
            ' ': '-'
        }

        # black_pieces = ['R','N','B','Q','K','B','N','R']
        # white_pieces = ['r','n','b','q','k','b','n','r']

        self.board = [
        ['R','N','B','Q','K','B','N','R'],
        ['P','P','P','P','P','P','P','P'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['p','p','p','p','p','p','p','p'],
        ['r','n','b','q','k','b','n','r'] 
        ]
        

    def print_board(self):
        # replace body with how you want your board printed
        # two iterations since its a 2D array
        for row in self.board:
            print("\n")
            for piece in row:
                print(self.symbols[piece], end=" ")
