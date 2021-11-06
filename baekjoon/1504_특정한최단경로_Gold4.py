import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
  dist = [987654321]*(N+1)
  dist[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    curC, curE = heapq.heappop(q)

    if dist[curE] < curC:
      continue
    
    for a, c in graph[curE]:
      newC = curC + c
      if newC < dist[a]:
        dist[a] = newC
        heapq.heappush(q, (newC, a))
  return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])
  graph[b].append([a, c])
v1, v2 = map(int, input().split())

start = dijkstra(1)
V1 = dijkstra(v1)
V2 = dijkstra(v2)
result = min(start[v1] + V1[v2] + V2[N], start[v2] + V2[v1] + V1[N])
print(result if result < 987654321 else -1)
  