T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    cnt = 0

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == M:
                    result += 1
                cnt = 0
    
    for j in range(N):
        for i in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or i == N-1:
                if cnt == M:
                    result += 1
                cnt = 0
    print('#{} {}'.format(tc, result))
