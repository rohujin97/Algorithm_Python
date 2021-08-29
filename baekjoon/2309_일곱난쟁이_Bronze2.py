from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort()

for dwarf in combinations(arr, 7):
    if sum(dwarf) == 100:
        for i in range(7):
            print(dwarf[i])
        break