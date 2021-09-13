# research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
# n = 2
# k = 2
research = ["xy","xy"]
n = 1
k = 1
# n일동안 매일 최소 k 번 이상 검색
def solution(research, n, k):
    answer = ''
    day = len(research)
    alpha = [[0 for _ in range(day)] for _ in range(26)]
    
    for i in range(day):
        for alp in research[i]:
            x = ord(alp) - 97
            alpha[x][i] += 1

    issue = [[] for _ in range(day)]
    # 매일 k 번 이상 검색
    for i in range(day):
        for j in range(26):
            if k <= alpha[j][i]:
                issue[i].append(j)
    t = 2*n*k
    
    final = [[]for _ in range(day-n+1)]
    #n일동안 총합이 t보다 크거나 같은지 확인
    for i in range(day-n+1):
        for j in range(len(issue[i])):
            if sum(alpha[issue[i][j]][i:i+n]) >= t:
                final[i].append(issue[i][j])

    total = [0]*26
    # 최고의 이슈 검색어 뽑기
    for i in range(len(final)):
        for j in range(len(final[i])):
            total[final[i][j]] += 1
    if sum(total) == 0:
        answer = 'None'
    else:
        answer = chr(total.index(max(total))+97)           
    return answer

print(solution(research, n, k))