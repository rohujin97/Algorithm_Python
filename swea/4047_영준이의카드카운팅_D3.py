T = int(input())

for tc in range(1, T+1):
    card = list(input())
    S = [0]*14
    D = [0]*14
    H = [0]*14
    C = [0]*14
    result = True
    for i in range(0, len(card), 3):
        num = int(card[i+1] + card[i+2])
        if card[i] == 'S':
            if S[num] != 0:
                result = False
                break
            S[num] = 1
        elif card[i] == 'D':
            if D[num] != 0:
                result = False
                break
            D[num] = 1
        elif card[i] == 'H':
            if H[num] != 0:
                result = False
                break
            H[num] = 1
        elif card[i] == 'C':
            if C[num] != 0:
                result = False
                break
            C[num] = 1
    if not result:
        print('#{} {}'.format(tc, 'ERROR'))
    else:
        print('#{} {} {} {} {}'.format(tc, 13-sum(S), 13-sum(D), 13-sum(H), 13-sum(C)))