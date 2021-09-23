from copy import deepcopy

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
leng = len(info)
parent = [0]*leng
sheep_wolf = [0, 0]
matrix = [[] for _ in range(leng)]
visited = [False]*leng

def dfs(v):
    visited[v] = True
    if info[v] == 0:
        sheep_wolf[0] += 1
    elif info[v] == 1:
        sheep_wolf[1] -= 1
    for child in matrix[v]:
        if not visited[child]:
            s_w = deepcopy(sheep_wolf)
            vis = deepcopy(visited)
            if check(child, s_w, vis):
                dfs(child)

def check(v, s_w, vis):
    vis[v] = True
    if info[v] == 0:
        s_w[0] += 1
    else:
        s_w[1] -= -1
    if sum(s_w) <= 0:
        return False
    for child in matrix[v]:
        if not vis[child]:
            check(child, s_w, vis)



def solution(info, edges):
    answer = 0

    for edge in edges:
        matrix[edge[0]].append(edge[1])
        parent[edge[1]] = edge[0]

    dfs(0)

    return answer



print(solution(info, edges))