# 백준 골드5 N-Queen
import sys
input = sys.stdin.readline
N = int(input())
col = [False] * (N)
slash = [False] *(2*N-1)
backSlash = [False] *(2*N-1)

cnt = 0

def nQueen(index):
    global N, cnt, col, slash, backSlash
    # N까지 다 채우면 끝
    if (index == N):
        cnt += 1
    else: 
        for i in range(N): # 가로, 대각선, 역대각선에 다른 퀸이 있는지 확인
            if not col[i] and not slash[index-i] and not backSlash[index+i]:
                col[i] = slash[index-i] = backSlash[index+i] = True
                nQueen(index+1)
                col[i] = slash[index-i] = backSlash[index+i] = False
            
nQueen(0)
print(cnt)