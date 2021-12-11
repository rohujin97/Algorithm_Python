n = 26

def solution(n):

    if n % 5 == 0:
        return n // 5
    else:
        answer = n // 5
        while answer >= 0:
            tmp = n - answer * 5
            if tmp % 3 == 0:
                return answer + tmp // 3
            answer -= 1
        return -1

print(solution(n))