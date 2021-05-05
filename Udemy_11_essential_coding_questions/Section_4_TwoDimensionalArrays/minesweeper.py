def mine_sweeper(bombs, num_rows, num_columns):
    field = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    for bomb in bombs:
        row = bomb[0]
        col = bomb[1]
        field[row][col] = -1
        for ii in range(row - 1, row + 2):
            for jj in range(col - 1, col + 2):
                if 0 <= ii < num_rows:
                    if 0 <= jj < num_columns:
                        if field[ii][jj] != -1:
                            field[ii][jj] += 1
    return field


print(mine_sweeper([[0, 0], [0, 1]], 3, 4))
