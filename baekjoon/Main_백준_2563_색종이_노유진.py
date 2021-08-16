import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(101)]for _ in range(101)]

for _ in range(N):
    c, r = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            if arr[i][j] == 0: # 겹치는 부분이 없을때
                arr[i][j] = 1
            elif arr[i][j] == 1: # 처음 겹치는 부분이 생길때
                arr[i][j] = 2

res = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1 or arr[i][j] == 2:
            res += 1
print(res)
