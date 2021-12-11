K = 3
user_scores = ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]

def check(rank, user):
    rank = sorted(rank.items(), key=(lambda x:x[1]), reverse=True)
    rank = dict(rank)
    for idx, key in enumerate(rank):
        if key == user[0]:
            return idx

def solution(K, user_scores):
    rank = dict()
    answer = 0

    for i in range(len(user_scores)):
        user = list(user_scores[i].split())
        user[1] = int(user[1])

        if not user[0] in rank:
            rank[user[0]] = user[1]
            if len(rank) <= K:
                answer += 1
            else:
                if check(rank, user) <= K-1:
                    answer += 1
        else:
            if rank[user[0]] < user[1]:
                before = check(rank, user)
                del rank[user[0]]
                rank[user[0]] = user[1]
                after = check(rank, user)
                if after <= K-1 and before != after:
                    print(user[0], after, before)
                    answer += 1
    return answer
print(solution(K, user_scores))