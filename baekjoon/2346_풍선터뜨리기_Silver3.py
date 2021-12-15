from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloon = deque(enumerate(map(int, input().split())))
result = []

while balloon:
    idx, cur = balloon.popleft()
    result.append(idx+1)
    if cur > 0:
        balloon.rotate(-(cur-1))
    elif cur < 0:
        balloon.rotate(-cur)

print(' '.join(map(str, result)))
