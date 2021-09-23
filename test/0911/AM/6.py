records = ["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"]
k = 10
date = "2020-03-05"

def solution(records, k, date):
    answer = []
    endD = int(date[-2:]) - 10
    endM = int(date[-5:-3])
    if endD <= 0:
        startD = 30 - abs(endD) + 1
        startM = endM - 1
        endD = abs(endD)
    else:
        startD = endD - 10 + 1
        startM  = endM
    
    
    # 기간내에 들어오는 records까지만 계산
    # pid에 구매한 uid번호 넣기(중복)
    # pid에 들어간 uid번호 보면서 재구매율 따지기
    pid = [[] for _ in range(10)]
    realP = set()
    # pid = [[] for _ in range(2)]
    for i in range(len(records)):
        m = int(records[i][5:7])
        d = int(records[i][8:10])
        if startM <= m <= endM and (startD <= d or d <= endD):
            p = int(records[i][-1])
            u = int(records[i][-6])
            pid[p].append(u)
            realP.append(p)

    for i in range(len(realP)):
        more = 0
        one = 0
        for j in range(len(pid[realP[i]])):
            


    return answer

solution(records, k, date)