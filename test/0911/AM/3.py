jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]

def solution(jobs):
    answer = []
    classN = [0]*101 # 분류번호
    jobN = [0]*10000
    time = []

    # time에 요청 시간에 맞는 번호 넣어주고
    # classN에 중요도 더해주고 
    # jobN에 들어와있음을 확인해주는 용도로 분류번호 넣기
    for i in range(len(jobs)):
        time.append(jobs[i][0])
        classN[jobs[i][2]] += jobs[i][3]
        jobN[i] = jobs[i][2]

    sec = 0
    index = 0
    end = [False]*len(jobs)
    while True:
        for i in range(len(time)):
            if sec == time[i]:

    
    
            

    return answer

solution(jobs)