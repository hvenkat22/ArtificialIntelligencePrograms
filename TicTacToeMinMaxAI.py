import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_val = move_val
            best_move = (i, j)

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)

        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already occupied. Try again.")
            continue

        if is_winner(board, 'X'):
            print_board(board)
            print("You Win!")
            break

        print("AI's move:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'O'

        if is_winner(board, 'O'):
            print_board(board)
            print("AI Wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

play_tic_tac_toe()