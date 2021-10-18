from itertools import combinations, permutations, product, combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [1, 2, 3, 4, 5, 6]

if M == 1:
    for i in product(arr, repeat = N):
        print(*i, sep=" ")
elif M == 2:
    for i in combinations_with_replacement(arr, N):
        print(*i, sep=" ")
elif M == 3:
    for i in permutations(arr, N):
        print(*i, sep=" ")