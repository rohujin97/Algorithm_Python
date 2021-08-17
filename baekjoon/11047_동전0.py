# 백준 실버2 동전0
import sys
input = sys.stdin.readline
N, money = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

cnt = 0 # 코인 개수
for i in range(N-1, -1, -1):
    if money == 0:
        break
    if money // coins[i] == 0:
        continue
    cnt += money // coins[i];
    money -= (money // coins[i]) * coins[i]
print(cnt)