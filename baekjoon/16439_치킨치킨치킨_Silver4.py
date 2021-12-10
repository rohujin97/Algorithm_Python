from itertools import permutations, combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(M)]

maxC = 0
for k in range(1, 4):
    for i in permutations(num, k):
        for ch in combinations_with_replacement(i, N):
            like = 0
            for j in range(N):
                like += chicken[j][ch[j]]
            maxC = max(maxC, like)
print(maxC)

