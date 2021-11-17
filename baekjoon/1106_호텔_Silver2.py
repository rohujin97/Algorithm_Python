import sys
input = sys.stdin.readline

INF = 987654321
C, N = map(int, input().split())
dp = [INF]*(C+101)
dp[0] = 0

for i in range(N):
    cost, person = map(int, input().split())
    for j in range(person, C+101):
        tmp = dp[j-person]
        if tmp != INF:
            dp[j] = min(dp[j], cost + tmp)

result = INF
for i in range(C, C+101):
    result = min(result, dp[i])
print(result)