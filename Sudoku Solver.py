import numpy as np
sudoku = np.array([[2,0,0,0,0,0,9,5,1],
                   [0,0,0,0,0,0,0,0,7],
                   [8,7,6,0,0,5,2,0,0],
                   [3,0,4,0,2,8,0,0,0],
                   [0,0,0,0,0,0,5,0,9],
                   [0,0,5,0,0,1,3,0,4],
                   [0,2,0,0,8,4,0,1,0],
                   [0,0,0,0,1,0,0,9,8],
                   [0,0,0,0,0,0,0,0,0]]).reshape(9,9)

def possible(y,x,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if sudoku[y][x]== 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return
    print(sudoku)
    input("More Possible Solutions?")

solve()
    
