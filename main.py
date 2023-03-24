import chess


if __name__ == "__main__":
    chess = chess.Chess()
    chess.board.print_board()

    black_pieces = ["P", "R", "N", "B", "Q"]
    white_pieces = ["p", "r", "n", "b", "q"]

    while True:
        print("\nTaking input of next move")
        try:
            # lets say move was f2 to f3
            # make sure input is always lowercase !
            white_turn = True # some variable to check turn ??
            # Also, check that piece is there at this location
            start = input("From: ")
            row0, col0 = ord(start[0].lower())-ord("a"), start[1]
            
            if chess.board.board[row0][col0] == "-":
                # print("Invalid starting position, enter again.")
                raise IndexError

            # Also, check that location is either empty or occupied by opponents piece 
            to = input("To: ")
            row1, col1 = ord(to[0].lower())-ord("a"), to[1]

            if white_turn == True:
                if chess.board.board[row0][col0] != "-" or chess.board.board[row0][col0] not in black_pieces:
                    # print("Invalid position, enter again.")
                    raise IndexError
                else:
                    white_turn = False 
                    break
            else:
                if chess.board.board[row0][col0] != "-" or chess.board.board[row0][col0] not in white_pieces:
                    # print("Invalid position, enter again.")
                    raise IndexError
                else:
                    white_turn = True
                    break
            

        except IndexError:
            print("Invalid move! Try again.")
            # continue

        if start == None or to == None:
            continue

        chess.move(start, to)

        # check for promotion pawns
        i = 0
        while i < 8:
            if not chess.turn and chess.board.board[0][i] != None and \
                chess.board.board[0][i].name == 'P':
                chess.promotion((0, i))
                break
            elif chess.turn and chess.board.board[7][i] != None and \
                chess.board.board[7][i].name == 'P':
                chess.promotion((7, i))
                break
            i += 1

        chess.board.print_board()
