T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr= [[] for _ in range(N)]
    arr[0] = [1]
    for i in range(1, N):
        tmp = arr[i-1]
        arr[i].append(1)
        for j in range(i-1):
            arr[i].append(tmp[j]+tmp[j+1])
        arr[i].append(1)
    print("#%d" %(test_case))
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()



