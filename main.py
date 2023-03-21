import chess


if __name__ == "__main__":
    chess = chess.Chess()
    chess.board.print_board()

    while True:
        start = input("From: ")
        to = input("To: ")
        
        '''
        start = translate(start)
        to = translate(to)'''

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