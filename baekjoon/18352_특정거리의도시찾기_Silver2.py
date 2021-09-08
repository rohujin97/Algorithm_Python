from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
street = [[]for _ in range(N+1)]
answer = [-1]*(N+1)
answer[X] = 0

for _ in range(M):
    x, y = map(int, input().split())
    street[x].append(y)

dist = deque([X])

while dist:
    cur = dist.popleft()
    for end in street[cur]:
        if answer[end] == -1:
            answer[end] = answer[cur] + 1
            dist.append(end)

if K not in answer:
    print(-1)
else:
    for i in range(N+1):
        if answer[i] == K:
            print(i)

