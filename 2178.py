# 미로탐색 - 백준

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [] 
for i in range(n):
    s.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
p = deque([[0, 0]])
s[0][0] = 1

while p:
    a, b = p.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            s[x][y] = s[a][b] + 1
            p.append([x, y])
            
print(s[n-1][m-1])