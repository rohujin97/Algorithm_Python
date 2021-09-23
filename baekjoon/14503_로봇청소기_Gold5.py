import sys
input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split())

dr = [0, 1, 0, -1] # 서 남 동 북
dc = [-1, 0, 1, 0]
dLeft = [0, 3, 2, 1] # 북 동 남 서 처음 왼쪽방향

arr = [list(map(int, input().split())) for _ in range(N)]

def findRoom(r, c, d, idx):
    global cnt
    visited = [0]*4
    for i in range(4):
        left = (dLeft[d] + i)%4
        nr = r + dr[left]
        nc = c + dc[left]
        if arr[nr][nc] == 1: # 벽일 경우
            visited[left] = 1
        elif arr[nr][nc] > 1: # 이미 청소한 경우
            visited[left] = 2
        elif arr[nr][nc] == 0: # 청소해야 하는 영역 발견
            cnt += 1
            arr[nr][nc] = idx
            if left == 0: nleft = 3 # 북의 왼쪽: 서
            elif left == 1: nleft = 2 # 서의 왼쪽: 남
            elif left == 3: nleft = 0 # 동의 왼쪽: 북
            elif left == 2: nleft = 1 # 남의 왼쪽: 동
            findRoom(nr, nc, nleft, idx+1)
            break
    if not 0 in visited: # 네 방향 모두 청소가 되어있거나 벽인 경우
        if d == 1: back = 0
        elif d == 0: back = 1
        elif d == 2: back = 3
        elif d == 3: back = 2
        if visited[back] == 1: 
            return
        elif visited[back] == 2:
            br = r + dr[back]
            bc = c + dc[back]
            findRoom(br, bc, d, idx)  

cnt = 1
arr[R][C] = 2
findRoom(R, C, D, 3)
print(cnt)