arr = list(input())

i = 0
start = 0
while i < len(arr):
    if arr[i] == "<":
        i += 1
        while i < len(arr) and arr[i] != ">":
            i += 1
        i += 1
    elif arr[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(arr) and arr[i].isalnum():
            i += 1
        tmp = arr[start:i]
        tmp.reverse()
        arr[start:i] = tmp
    elif arr[i] == " ":
        i += 1
print(''.join(arr))
