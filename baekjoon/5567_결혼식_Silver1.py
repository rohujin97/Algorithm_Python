n = int(input())
m = int(input())

friend = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    friend[x].append(y)
    friend[y].append(x)

invite = []

def DFS(index, cnt):
    visited[index] = True
    if cnt == 2:
        return
    for nx in friend[index]:
        if not visited[nx]:
            invite.append(nx)
        DFS(nx, cnt + 1)

DFS(1, 0)
print(len(invite))