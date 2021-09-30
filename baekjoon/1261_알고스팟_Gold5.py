import sys, heapq
input = sys.stdin.readline
INF = 987654321

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(i, j):
    q = []
    heapq.heappush(q, (0, i, j))
    wall = [[INF]*M for _ in range(N)]
    wall[i][j] = 0

    while q:
        w, r, c = heapq.heappop(q)

        if r == N-1 and c == M-1:
            return w

        if wall[r][c] < w: continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 > nr or nr >= N or 0 > nc or nc >= M: continue
            new_wall = miro[nr][nc] + w
            if wall[nr][nc] > new_wall:
                wall[nr][nc] = new_wall
                heapq.heappush(q, (new_wall, nr, nc))

M, N = map(int, input().split())
miro = [[0]*M for _ in range(N)]

for i in range(N):
    st = input()
    for j in range(M):
        miro[i][j] = int(st[j])

print(dijkstra(0, 0))
