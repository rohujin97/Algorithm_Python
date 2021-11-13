A = [5, 3, 10, 6, 11]

def solution(A):
    list1 = []
    list2 = []

    for i in A:
        if i % 2 == 0:
            list1.append(i)
        else:
            list2.append(i)


    max1 = 0 if not list1 else max(list1)
    max2 = 0 if not list2 else max(list2)
    return(max1 + max2)

print(solution(A))
