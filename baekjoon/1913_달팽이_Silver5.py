import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(input())
T = int(input())

snail = [[0]*N for _ in range(N)]
start = N**2
r, c = 0, 0
d = 0
tr, tc = 0, 0

while start > 0:
    if start == T:
        tr, tc = r+1, c+1
    snail[r][c] = start
    start -= 1
    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
        d = (d + 1) % 4
        r += dr[d]
        c += dc[d]
    else:
        r = nr
        c = nc

for n in snail:
    print(' '.join(map(str, n)))
print(tr, tc)