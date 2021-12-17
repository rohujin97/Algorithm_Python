import sys
input = sys.stdin.readline

N = int(input())
cow = [-1]*11
cnt = 0

for _ in range(N):
    num, street = map(int, input().split())

    if cow[num] == -1:
        cow[num] = street
    else:
        if cow[num] != street:
            cow[num] = street
            cnt += 1

print(cnt)