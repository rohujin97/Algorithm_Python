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

while start > 0:
    if start == T:
        tr, tc = r+1, c+1
    snail[r][c] = start
    start -= 1

    if r + dr[d] < 0 or r + dr[d] >= N or c + dc[d] < 0 or c + dc[d] >= N or snail[r+dr[d]][c+dc[d]] != 0:
        d = (d + 1) % 4
    r += dr[d]
    c += dc[d]

for n in snail:
    print(' '.join(map(str, n)))
print(tr, tc)