n = 3
m = 4
puddles = [[2, 2]]

def solution(m, n, puddles):
    dp = [[1]*m for _i in range(n)]
    
    for x,y in puddles:
        dp[y-1][x-1] = 0
        if x-1 == 0:
            for k in range(y-1,n):
                dp[k][0]=0
        if y-1 == 0:
            for k in range(x-1,m):
                dp[0][k]=0

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n-1][m-1]
    return answer%1000000007

print(solution(m, n, puddles))