n = int(input())
stu = list(map(int, input().split()))
li = [1]

for i in range(1, n):
    li.insert(i - stu[i], i+1)
    
print(' '.join(map(str, li)))