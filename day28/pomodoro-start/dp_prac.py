
board = [list(map(int,input().split())) for _ in range(8)]

new_board = [[0 for _ in range(8)] for _ in range(8)]

def is_range(row,column):
    return 0 <= row < 8 and 0 <= column < 8

for r in range(8):
    for c in range(8):
        if is_range(r-1,c) and is_range(r,c-1):
            new_board[r][c] = max(new_board[r-1][c] + board[r][c], new_board[r][c-1] + board[r][c])
        elif is_range(r-1,c) and not is_range(r,c-1):
            new_board[r][c] = new_board[r-1][c] + board[r][c]
        elif not is_range(r-1,c) and is_range(r,c-1):
            new_board[r][c] = new_board[r][c-1] + board[r][c]
        else:
            new_board[r][c] = board[r][c]

print(*new_board, sep='\n')
