T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    result = 1
    for i in range(9):
        check = [0]*10
        down = [0]*10
        for j in range(9):
            check[sudoku[i][j]] = 1
            down[sudoku[j][i]] = 1
        if sum(check) != 9 or sum(down) != 9:
            result = 0
            break
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            total = 0
            for k in range(3):
                total += sum(sudoku[i+k][j:j+3])
            if total != 45:
                result = 0
                break
        if result == 0:
            break

    print('#{} {}'.format(tc, result))