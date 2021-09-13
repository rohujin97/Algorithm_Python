# n = 437674
# k = 3
n = 110011
k = 10

import math

def sosu(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, k):
    answer = 0
    num = str(change(n, k))

    nums = ""
    for i in range(len(num)):
        print(answer, nums)
        if num[i] == '0':
            if sosu(int(nums)):
                answer += 1
            nums = ""
        nums += num[i]
    if nums != "":
        if sosu(int(nums)):
            answer += 1
    return answer

print(solution(n, k))