from itertools import permutations
v = [20, 8, 10, 1, 4, 15]

def solution(v):
    maxV = 0
    for per in permutations(v, len(v)):
        result = 0
        for i in range(len(v)-1):
            result += abs(per[i] - per[i+1])
        maxV = max(maxV, result)
    return maxV

print(solution(v))