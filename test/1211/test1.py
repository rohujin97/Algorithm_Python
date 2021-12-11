vote = "ABBCCCBBAB"

def solution(vote):
    team = [0]*3
    result = list(vote)

    for i in range(len(result)):
        if result[i] == 'A':
            team[0] += 1
        elif result[i] == 'B':
            team[1] += 1
        else:
            team[2] += 1
    if team[2] >= len(result)//2:
        return 'C'
    else:
        if team[0] == team[1]:
            return 'AB'
        elif team[0] > team[1]:
            return 'A'
        elif team[0] < team[1]:
            return 'B'

print(solution(vote))
