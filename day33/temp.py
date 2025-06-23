n, m, q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

winds = [list(map(int, input().split())) for _ in range(q)]


def shift(r1, c1, r2, c2):
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    temp_list = []

    # north
    for c in range(c1, c2 + 1):
        temp_list.append(grid[r1][c])
    # east
    for r in range(r1 + 1, r2 + 1):
        temp_list.append(grid[r][c2])
    # south
    for c in reversed(range(c1, c2)):
        temp_list.append(grid[r2][c])
    # west
    for r in reversed(range(r1 + 1, r2)):
        temp_list.append(grid[r][c1])

    shift_list = [temp_list[-1]] + temp_list[0:-1]
    cnt_idx = 0
    for c in range(c1, c2 + 1):
        grid[r1][c] = shift_list[cnt_idx]
        cnt_idx += 1
    # east
    for r in range(r1 + 1, r2 + 1):
        grid[r][c2] = shift_list[cnt_idx]
        cnt_idx += 1
    # south
    for c in reversed(range(c1, c2)):
        grid[r2][c] = shift_list[cnt_idx]
        cnt_idx += 1
    # west
    for r in reversed(range(r1 + 1, r2)):
        grid[r][c1] = shift_list[cnt_idx]
        cnt_idx += 1


def is_range(r, c):
    return 0 <= r < n and 0 <= c < m


def avg(r, c):
    temp = 0
    count = 0
    drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dr, dc in zip(drs, dcs):
        n_r, n_c = r + dr, c + dc
        if is_range(n_r, n_c):
            temp += grid[n_r][n_c]
            count += 1
    return temp // count


def change_avg(r1, c1, r2, c2):
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    temp_board = [[0 for _ in range(m)] for _ in range(n)]
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            temp_board[r][c] = avg(r, c)

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            grid[r][c] = temp_board[r][c]


for i in range(q):
    r1, c1, r2, c2 = winds[i]
    shift(r1, c1, r2, c2)
    # change_avg(r1,c1,r2,c2)

print(*grid, sep='\n')



