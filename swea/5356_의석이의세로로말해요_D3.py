T = int(input())

for test_case in range(1, T+1):
    letter =[list(input()) for _ in range(5)]
    max_l = 0
    for i in range(5):
        if max_l < len(letter[i]):
            max_l = len(letter[i])

    result = ''
    for i in range(max_l):
        for j in range(5):
            if i < len(letter[j]):
                result += letter[j][i]
    print('#{} {}'.format(test_case, result))