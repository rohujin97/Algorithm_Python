lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# result = [3, 5]

def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero = lottos.count(0)

    for i in win_nums:
        if i in lottos:
            cnt += 1

    return rank[zero+cnt], rank[cnt]

print(solution(lottos, win_nums))