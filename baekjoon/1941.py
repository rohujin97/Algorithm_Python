arr = [[] for _ in range(5)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
visited = [[0 for _ in range(5)] for _ in range(5)]
total = 0
for i in range(5):
    st = input()
    arr[i] = list(st)
    
# DFS로 7번 상하좌우 보면서 s 4개있는지 확인
def BFS():
    cnt = 0
    q = [(a, b)]
    visited[a][b] = 1
    for _ in range(7):
        x, y = q.pop(0)
        if arr[x][y] == 'S':
            cnt += 1
        if cnt == 4:
            total += 1
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                q.append((nx, ny))
                visited[nx][ny] = 0
    return

DFS(0, 0)
print(total)