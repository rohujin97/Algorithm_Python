student = [0, 1, 0, 0, 1, 1, 0]
k = 2
answer = 0

def solution(student, k):
    for i in range(len(student)):
        check(i)
    print(answer)
    return answer

def check(index):
    global answer
    group = []
    for i in range(index, len(student)):
        group.append(student[i])
        if sum(group) == k:
            answer += 1
        elif sum(group) > k:
            return

solution(student, k)