n = int(input())
arr = []
for i in range(1, n+1):
    st = str(int(input()))
    cnt = 0
    cur = "0"
    for j in st:
        if j != cur:
            cnt += 1
            cur = j
    print('#%d %d' %(i, cnt))