fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
import math

parking = []
car = [[] for _ in range(10000)]

def solution(fees, records):
    time = dict()
    
    for i in range(len(records)):
        rec = records[i].split(" ")
        carN = int(rec[1])
        if rec[2] == "IN":
            car[carN].append(rec[0])
            parking.append(carN)
        else:
            _in = car[carN].pop().split(":")
            _out = rec[0].split(":")
            check(carN, _in, _out, time)

    leng = len(parking)
    end = "23:59".split(":")
    if leng > 0:
        for i in range(leng):
            start = car[parking[0]][0].split(":")
            check(parking[0], start, end, time)
    
    total = []
    tim = dict(sorted(time.items()))
    for key in tim.keys():
        if tim[key] <= fees[0]:
            pay = fees[1]
        else:
            pay = fees[1] + math.ceil((tim[key]-fees[0])/fees[2])*fees[3]
        total.append(pay)
    return total
    

def check(carN, _in, _out, time):
    global parking
    parking.remove(carN)
    inH = int(_in[0])
    inM = int(_in[1])
    outH = int(_out[0])
    outM = int(_out[1])
    total = (outH - inH)*60 + (outM - inM)
    if not carN in time:
        time[carN] = total
    else:
        time[carN] += total

solution(fees, records)