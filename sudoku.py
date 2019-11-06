sudokuCorrect = [[8, 1, 2, 7, 5, 3, 6, 4, 9],
                 [9, 4, 3, 6, 8, 2, 1, 7, 5],
                 [6, 7, 5, 4, 9, 1, 2, 8, 3],
                 [1, 5, 4, 2, 3, 7, 8, 9, 6],
                 [3, 6, 9, 8, 4, 5, 7, 2, 1],
                 [2, 8, 7, 1, 6, 9, 5, 3, 4],
                 [5, 2, 1, 9, 7, 4, 3, 6, 8],
                 [4, 3, 8, 5, 2, 6, 9, 1, 7],
                 [7, 9, 6, 3, 1, 8, 4, 5, 2]]

# First row and first box have two 9
sudokuWrong   = [[8, 9, 2, 7, 5, 3, 6, 4, 9],
                 [9, 4, 3, 6, 8, 2, 1, 7, 5],
                 [6, 7, 5, 4, 9, 1, 2, 8, 3],
                 [1, 5, 4, 2, 3, 7, 8, 9, 6],
                 [3, 6, 9, 8, 4, 5, 7, 2, 1],
                 [2, 8, 7, 1, 6, 9, 5, 3, 4],
                 [5, 2, 1, 9, 7, 4, 3, 6, 8],
                 [4, 3, 8, 5, 2, 6, 9, 1, 7],
                 [7, 9, 6, 3, 1, 8, 4, 5, 2]]

def check_flag(flag):
    for i in flag:
        if not i:
            return False
    return True

def check_row(s, row):
    flag = [False for i in range(9)]
    for i in s[row]:
        if flag[i-1]:
            return False
        flag[i-1] = True
    return check_flag(flag)

def check_col(s, col):
    flag = [False for i in range(9)]
    for i in range(9):
        if flag[s[i][col]-1]:
            return False
        flag[s[i][col]-1] = True
    return check_flag(flag)

def check_box(s, row, col):
    flag = [False for i in range(9)]
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if flag[s[i][j]-1]:
                return False
            flag[s[i][j]-1] = True
    return check_flag(flag)

def check_all_row(s):
    for i in range(9):
        if not check_row(s, i):
            return False
    return True

def check_all_col(s):
    for i in range(9):
        if not check_col(s, i):
            return False
    return True
