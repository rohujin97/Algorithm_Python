def check(nr, nc, r, c):
    for i in range(1, 5):
        if pan[r + (nr * i)][c + (nc * i)] != 'o':
            return False
    return True

def find():
    for r in range(N):
        for c in range(N):
            if pan[r][c] != 'o': continue
            # 열 오목
            if c + 4 < N and check(0, 1, r, c):
                return 'YES'
            # 행 오목
            if r + 4 < N and check(1, 0, r, c):
                return 'YES'
            # 역대각선(|) 오목
            if c - 4 >= 0 and r - 4 >= 0 and check(-1, -1, r, c):
                return 'YES'
            # 정대각선(/) 오목
            if c + 4 < N and r - 4 >= 0 and check(-1, 1, r, c):
                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(input()) for _ in range(N)]
    answer = find()
    print('#{} {}'.format(tc, answer))


