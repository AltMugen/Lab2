def chess_board(n, m):
    board = [['.' if (i+j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]
    return board

def z3():
    board = chess_board(3, 3)
    for row in board:
        print(' '.join(row))
