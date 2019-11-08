import multiprocessing as mp
import time

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
    time.sleep(0.1)
    print("Start check_row method with row " + str(row))
    flag = [False for i in range(9)]
    for i in s[row]:
        if flag[i-1]:
            print("End check_row method with return value False")
            return False
        flag[i-1] = True
    final_flag = check_flag(flag)
    print("End check_row method with return value " + str(final_flag))
    return final_flag

def check_col(s, col):
    time.sleep(0.1)
    print("Start check_col method with col " + str(col))
    flag = [False for i in range(9)]
    for i in range(9):
        if flag[s[i][col]-1]:
            print("End check_col method with return value False")
            return False
        flag[s[i][col]-1] = True
    final_flag = check_flag(flag)
    print("End check_col method with return value " + str(final_flag))
    return final_flag

def check_box(s, row, col):
    time.sleep(0.1)
    print("Start check_box method with row " 
           + str(row) + " and col " + str(col))
    flag = [False for i in range(9)]
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if flag[s[i][j]-1]:
                print("End check_box method with return value False")
                return False
            flag[s[i][j]-1] = True
    final_flag = check_flag(flag)
    print("End check_box method with return value " + str(final_flag))
    return final_flag

def check_all_row(s):
    print("Start check_all_row method")
    for i in range(9):
        if not check_row(s, i):
            print("End check_all_row method with return value False")
            return False
    print("End check_all_row method with return value True")
    return True

def check_all_col(s):
    print("Start check_all_col method")
    for i in range(9):
        if not check_col(s, i):
            print("End check_all_col method with return value False")
            return False
    print("End check_all_col method with return value True")
    return True

def get_flag(flag):
    result.append(flag)

def terminate_callback(flag):
    fastestResult.append(flag)
    if not flag:
        pool.terminate()

def check_sudoku_parallel(s, callback):
    global pool
    pool = mp.Pool(mp.cpu_count())
    pool.apply_async(check_all_col, (s,), callback=callback)
    pool.apply_async(check_all_row, (s,), callback=callback)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            pool.apply_async(check_box, (s, i, j,), callback=callback)
    pool.close()
    pool.join()

def check_sudoku_slow(s):
    global result
    start = time.time()
    result = []
    print("----slow-----------------------------------------------------------")
    check_sudoku_parallel(s, get_flag)
    print("Result List:")
    print(result)
    print("Final Result:")
    print(check_flag(result))
    print("duration " + str(time.time() - start))
    print("-------------------------------------------------------------------")

def check_sudoku_fast(s):
    global fastestResult
    start = time.time()
    fastestResult = []
    print("----fast-----------------------------------------------------------")
    check_sudoku_parallel(s, terminate_callback)
    print("Result List:")
    print(fastestResult)
    print("Final Result:")
    print(check_flag(fastestResult))
    print("duration " + str(time.time() - start))
    print("-------------------------------------------------------------------")

def read_multiple_int():
    return [int(x) for x in input().split(' ')]

def read_sudoku_from_terminal():
    s = []
    for _ in range(9):
        s.append(read_multiple_int())
    return s

if __name__ == '__main__':
    check_sudoku_slow(sudokuCorrect)
    check_sudoku_slow(sudokuWrong)

    check_sudoku_fast(sudokuCorrect)
    check_sudoku_fast(sudokuWrong)
