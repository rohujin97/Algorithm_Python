t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_p = 0

    # 더했을때 영역안으로 들어올 수 있는 영역까지
    for i in range(n-m+1):
        for j in range(n-m+1):
            hap = 0 # m*m범위 안에 있는 값들을 더할 변수
            for a in range(i, i+m): # m*m 범위안으로 더하기
                for b in range(j, j+m):
                    hap += arr[a][b]
            max_p = max(max_p, hap)
    print('#{} {}'.format(tc, max_p))