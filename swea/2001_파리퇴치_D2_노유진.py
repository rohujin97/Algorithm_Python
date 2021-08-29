T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    size = N - M + 1
    maxV = 0
    for i in range(size):
        for j in range(size):
            total = 0
            for k in range(M):
                total += sum(matrix[i+k][j:j+M])
            maxV = max(maxV, total)
    print('#{} {}'.format(tc, maxV))   
                