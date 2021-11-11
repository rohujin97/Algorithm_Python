import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
INF = 987654321

graph = [[INF]*N for _ in range(N)]

for _ in range(M):
	a, b, c = map(int, input().split())
	if graph[a-1][b-1] > c:
		graph[a-1][b-1] = c

for k in range(N):
	for i in range(N):
		for j in range(N):
			if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
	for j in i:
		if j == INF:
			print(0, end=' ')
		else:
			print(j, end=' ')
	print()