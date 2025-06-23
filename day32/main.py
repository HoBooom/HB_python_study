grid = [                           # 3*8행렬
    [6, 7, 12, -5, 5, 3, 11, 3],   # 1행
    [-8, 10, 14, 9, 7, 13, 8, 5],  # 2행
    [11, 12, 7, 4, 8, -2, 9, 4]    # 3행
]

pebble_sum_table = [[0 for _ in range(8)] for _ in range(4)]

def w(p,i):
    if p == 0:
        return grid[0][i]
    elif p == 1:
        return grid[1][i]
    elif p == 2:
        return grid[2][i]
    elif p == 3:
        return grid[0][i] + grid[2][i]

def pebble(n):
    for p in range(4):
        pebble_sum_table[p][0] = w(p,0)
    for i in range(1,n + 1):
        for p in range(4):
            pebble_sum_table[p][i] = w(p,i)

