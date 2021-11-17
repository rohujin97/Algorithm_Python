import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 100*100
dp = [0]*(INF+1)

C, N = map(int, input().split())
cost = [0]*21
person = [0]*21
maxP = 0

for i in range(N):
    a, b = map(int, input().split())
    cost[i] = a
    person[i] = b

for i in range(1, N+1):
    for j in range(cost[i], INF+1):
        dp[j] = dp[j-cost[i]] + person[i] if dp[j] < dp[j - cost[i]] + person[i] else dp[j]

for i in range(1, INF+1):
    if dp[i] >= C:
        print(i)
        break
