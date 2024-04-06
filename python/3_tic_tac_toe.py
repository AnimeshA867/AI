import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))
    return moves

def evaluate(board):
    for player in ['X', 'O']:
        if check_winner(board, player):
            return 1 if player == 'X' else -1
    return 0

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or check_winner(board, 'X') or check_winner(board, 'O') or len(available_moves(board)) == 0:
        return evaluate(board)
    
    if maximizing_player:
        max_eval = -math.inf
        for move in available_moves(board):
            row, col = move
            board[row][col] = 'X'
            eval = minimax(board, depth - 1, False, alpha, beta)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            row, col = move
            board[row][col] = 'O'
            eval = minimax(board, depth - 1, True, alpha, beta)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for move in available_moves(board):
        row, col = move
        board[row][col] = 'X'
        eval = minimax(board, 5, False, alpha, beta)
        board[row][col] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    while True:
        print_board(board)
        move = input("Enter your move (row,col): ")
        row, col = map(int, move.split(','))
        if board[row][col] == " ":
            board[row][col] = "O"
            if check_winner(board, "O"):
                print_board(board)
                print("You win!")
                break
            if len(available_moves(board)) == 0:
                print_board(board)
                print("It's a tie!")
                break
            print("Computer's turn:")
            comp_row, comp_col = get_best_move(board)
            board[comp_row][comp_col] = "X"
            if check_winner(board, "X"):
                print_board(board)
                print("Computer wins!")
                break
        else:
            print("Invalid move. Try again.")

tic_tac_toe()
