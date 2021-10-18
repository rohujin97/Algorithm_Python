T = int(input())


def getJohapDfs(lev, sum):
    for i in nums:
        nxt = sum * 10 + i
        if nxt > 999: continue
        if JohapUsed[nxt] == 1: continue
        JohapUsed[nxt] = 1
        getJohapDfs(lev+1, nxt)

def getJohap():
    global joCnt
    getJohapDfs(0, 0)

    for i in range(1000):
        if JohapUsed[i] == 0: continue
        Johap[joCnt] = i

        if i < 10: JohapMinCnt[joCnt] = 1
        elif i < 100: JohapMinCnt[joCnt] = 2
        elif i < 1000: JohapMinCnt[joCnt] = 3
        
        joCnt += 1

def init():
    for i in range(joCnt):
        num = Johap[i]
        best[num] = JohapMinCnt[i]

def getCntResult(a, oper, b):
    if oper == "+": return a + b
    elif oper == "-": return a - b
    elif oper == "*": return a * b
    return a // b

def getMinTouchCnt(touchCnt, now):
    for x in opers:
        for i in range(joCnt):
            num = Johap[i]
            nxtCnt = touchCnt + JohapMinCnt[i] + 1
            
            if nxtCnt > M - 1: break
            if x == "/" and num == 0: continue

            nxt = getCntResult(now, x, num)
            if x == "+" and nxt > 999: break
            if x == "-" and nxt < 0: break
            if x == "*" and nxt > 999: break
            if used[nxt] == 1: continue
            if best[nxt] <= nxtCnt: continue

            best[nxt] = nxtCnt
            used[nxt] = 1
            getMinTouchCnt(nxtCnt, nxt)
            used[nxt] = 0


for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    oper_num = list(map(int, input().split()))
    W = int(input())

    Johap = [0]*1000
    JohapUsed = [0]*1000
    JohapMinCnt = [0]*1000
    best = [99]*1000
    used = [0]*1000
    opers = []
    for i in range(O):
        if oper_num[i] == 1: opers.append("+")
        elif oper_num[i] == 2: opers.append("-")
        elif oper_num[i] == 3: opers.append("*")
        else: opers.append("/")

    joCnt = 0
    getJohap()
    init()

    if best[W] != 99: answer = best[W]
    else:
        for i in range(joCnt):
            getMinTouchCnt(JohapMinCnt[i], Johap[i])
        answer = best[W] + 1
    
    if best[W] == 99:
        answer = -1
    print("#%d %d" %(tc, answer))


