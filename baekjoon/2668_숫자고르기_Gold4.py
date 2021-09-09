import heapq
from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
first = [i for i in range(N+1)]
second = [0]
for _ in range(N):
    second.append(int(input()))

visited = []

def DFS(start, index): # 본인이 빠져나오는지 확인
    if start == index:
        result.append(start)
        return
    if visited[index]:
        return
    visited[index] = True
    DFS(start, second[index])

result = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    visited[i] = True
    DFS(i, second[i])
        
print(len(result))
for num in result:
    print(num)
