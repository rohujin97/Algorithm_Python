# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

def solution(id_list, report, k):
    answer = dict()

    dec = [[] for _ in range(len(report))]
    d = dict()
    for i in range(len(id_list)):
        d[id_list[i]] = 0
        answer[id_list[i]] = 0
    
    total = []
    send = [[] for _ in range(len(id_list))]
    report = list(set(report))
    for i in range(len(report)):
        dec[i] = report[i].split(" ")
        total.append(dec[i])
        send[id_list.index(dec[i][1])].append(dec[i][0])
        d[dec[i][1]] += 1

    for i in range(len(d)):
        if d[id_list[i]] >= k: # 신고횟수를 넘긴다면
            for msg in send[id_list.index(id_list[i])]:
                answer[msg] += 1

    print(list(answer.values()))
    return list(answer.values())

solution(id_list, report, k)