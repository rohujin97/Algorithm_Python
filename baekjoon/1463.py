# 1로 만들기 - 백준

import sys
input = sys.stdin.readline
n = int(input())
k = [0 for i in range(n+1)] # 인덱스에 도달하는데 걸리는 최소 카운팅 저장 배열

for i in range(2, n+1):
    k[i] = k[i-1] + 1
    if (i % 3 == 0 and k[i] > k[i//3] + 1): # 3으로 나눠서 온 카운팅이 더 작으면 i를 3 나눈 인덱스의 최소 카운팅 + 1 
        k[i] = k[i//3] + 1
    if (i % 2 == 0 and k[i] > k[i//2] + 1):
        k[i] = k[i//2] + 1

print(k[n])