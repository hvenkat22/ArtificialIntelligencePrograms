def print_board(board):
    for i in range(9):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j%3==0 and j!=0:
                print("|",end=" ")
            print(board[i][j],end=" ")
        print()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3*(row//3),3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col] == num:
                return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None, None

def solve_sudoku(board):
    row,col=find_empty_location(board)

    if row is None and col is None:
        return True
    for num in range(1,10):
        if is_valid(board,row,col, num):
            board[row][col]=num
            
            if solve_sudoku(board):
                return True
            
            board[row][col]=0

    return False
sudoku_board = [
    [5,0,0,0,7,0,0,0,0],
    [6,0,0,0,9,0,0,0,0],
    [0,9,8,0,0,0,0,0,0],
    [7,0,0,0,0,0,0,0,4],
    [0,3,0,0,0,0,6,0,0],
    [0,0,4,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0],
    [9,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0]
]
solve_sudoku(sudoku_board)
print_board(sudoku_board)
