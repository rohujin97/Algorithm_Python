n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
import heapq

def dijkstra(dest, graph, start):
    dest[start] = 0
    q = []

    heapq.heappush(q, (0, start))
    while q:
        cost, cur = heapq.heappop(q)

        if dest[cur] < cost:
            continue

        for nx in graph[cur]:
            nxCost = cost + 1
            if nxCost < dest[nx]:
                dest[nx] = nxCost
                heapq.heappush(q, (nxCost, nx))

def solution(n, edge):
    answer = 0
    INF = 987654321

    dest = [INF]*n
    graph = [[] for _ in range(n)]

    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    dijkstra(dest, graph,  0)

    maxD = max(dest)
    for i in range(1, n):
        if maxD == dest[i]:
            answer += 1
    return answer

print(solution(n, edge))