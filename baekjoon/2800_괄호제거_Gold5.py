import sys
from itertools import combinations
input = sys.stdin.readline

str = list(input().rstrip())
left, twin = [], []

for i, s in enumerate(str):
    if s == '(':
        str[i] = ''
        left.append(i)
    elif s ==')':
        str[i] = ''
        twin.append([left.pop(), i])

result = set()

for i in range(len(twin)):
    for j in combinations(twin, i):
        tmp = str[:]
        for l, r in j:
            tmp[l] = '('
            tmp[r] = ')'
        result.add(''.join(tmp))
for i in sorted(result):
    print(i)