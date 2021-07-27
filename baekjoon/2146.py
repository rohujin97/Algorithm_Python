# 다리 만들기 - 백준

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs1(x, y, cnt):
    q.append([x, y])
    val[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <n:
                if map[nx][ny] == 1 and val[nx][ny] == 0:
                    val[nx][ny] = cnt
                    q.append([nx, ny])

def bfs2(num):
    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] == 1 and val[nx][ny] != num:
                    return val2[x][y] - 1
                if map[nx][ny] == 0 and val2[nx][ny] == 0:
                    val2[nx][ny] = val2[x][y] + 1
                    q2.append([nx, ny])
    
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
val = [[0]*n for _ in range(n)]
ans = sys.maxsize
cnt = 1
q = deque()

# 섬 몇개인지 알아보기
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and val[i][j] == 0:
            bfs1(i, j, cnt)
            cnt += 1

# 각 섬별로 다른 섬과 닿을때까지 크기 늘리기
for k in range(1, cnt):
    q2 = deque()
    val2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1 and val[i][j] == k:
                q2.append([i, j])
                val2[i][j] = 1
    res = bfs2(k)
    ans = min(ans, res)
print(ans)