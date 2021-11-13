# A = [1, 1, 3, 4, 4, 4]
# A = [1, 2, 2, 2, 5, 5, 5, 8]
A = [1, 1, 1,1, 3, 3, 4, 4, 4, 4, 4]
def solution(A):
    dict = {}
    for i in A:
        if not i in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

    total = 0
    for i in dict.keys():
        zero = dict[i]
        full = i - dict[i]
        if i != dict[i]:
            if zero > abs(full):
                total += abs(full)
            else:
                total += zero
    return total



print(solution(A))