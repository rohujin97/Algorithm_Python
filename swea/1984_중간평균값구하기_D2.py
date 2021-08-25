T = int(input())
for t in range(1, T+1):
    num = sorted(list(map(int, input().split())))
    total = sum(num[1:9])
    avg = round(total/8)
    
    print("#%d %d" %(t, avg))
