# 달팽이 숫자 - swea

def snail(arr, start, length, num): # 상하좌우 for 문 차례대로 반복
    end = start + length-1
    for h in range(start, end + 1):
        arr[start][h] = num
        num += 1
    for w in range(start + 1, end + 1):
        arr[w][end] = num
        num += 1
    for h in range(end - 1, start -1, -1):
        arr[end][h] = num
        num += 1
    for w in range(end -1, start, -1):
        arr[w][start] = num
        num += 1
    return num

T = int(input())    
for test_case in range(1, T + 1):
    size = int(input())
    arr = [[0 for _ in range(size)] for _ in range(size)]
    num, start = 1, 0
    
    while size > 0:
        num = snail(arr, start, size, num)
        size -= 2 #점점 박스가 -2만큼 줄음
        start += 1 #시작위치는 0 -> 1 -> 2 으로 1씩 증가
    print("#{}".format(test_case))
    for r in arr:
        print(*r)
    print()