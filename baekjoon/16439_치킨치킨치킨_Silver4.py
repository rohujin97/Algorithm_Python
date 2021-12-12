import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(M)]

maxC = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            sumC = 0
            for n in range(N):
                sumC += max(chicken[n][i], max(chicken[n][j], chicken[n][k]))
            maxC = sumC if maxC < sumC else maxC

print(maxC)

