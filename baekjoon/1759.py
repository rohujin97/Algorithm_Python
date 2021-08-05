# 암호만들기 - 백준

from itertools import combinations

n, m = map(int, input().split())
arr = list(input().split())
arr.sort()

def check(str):
    cnt = 0
    for alpha in str: # 모음 몇개있는지 체크
        if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
            cnt += 1
    return cnt

for c in combinations(arr, n):
    if check(c) >=1 and (len(c) - check(c)) >= 2: # 모음 개수가 1이상이고 자음 개수가 2이상일때
        print(''.join(c))
