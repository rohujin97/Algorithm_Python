# 트리의 부모 찾기 - 백준
import sys
input = sys.stdin.readline

#   root부터 마지막 자식순으로 탐색
def DFS(graph, start, parent):
    q = [start]
    while q:
        node = q.pop()
        for i in graph[node]:
            parent[i].append(node) #node가 부모 i가 자식
            q.append(i)
            graph[i].remove(node) #자식에게도 있는 중복된 값 처리
    return parent

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range(n-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in list(DFS(graph, 1, parent))[2:]:
    print(i[0])