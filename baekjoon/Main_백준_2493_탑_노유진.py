n = int(input())
arr = list(map(int, input().split()))
res = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]: # stack에 있는 값이 오른쪽에 있는 탑보다 작을때까지
            res.append(stack[-1][0] + 1)  # stack값보다 작은 탑들에게 그 값의 index 넣기
            break
        else:
            stack.pop() # 크거나 같은 값 나오면 pop
    if not stack: # stack이 비면 수신할 탑이 없음
        res.append(0)
    stack.append([i, arr[i]]) 

print(" ".join(map(str, res)))