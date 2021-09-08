import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
street = [[]for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    street[x].append(y)

dist = []
heapq.heappush(dist, (0, X))
num = []
while dist:
    cnt, start = heapq.heappop(dist)
    if visited[start]: continue

    if cnt == K:
        heapq.heappush(num, start)

    visited[start] = True
    for end in street[start]:
        if not visited[end]:
            heapq.heappush(dist, (cnt+1, end))

if len(num) > 0:
    for i in num:
        print(i)
else:
    print(-1)

