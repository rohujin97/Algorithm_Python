import sys
input = sys.stdin.readline

N, M = map(int, input().split())
walls = list(map(int, input().split()))
result = 0

for i in range(1, M-1):
    start = end = 0

    for j in range(0, i):
        start = max(start, walls[j])

    for j in range(i+1, M):
        end = max(end, walls[j])

    if walls[i] < start and walls[i] < end:
        result += min(start, end) - walls[i]

print(result)