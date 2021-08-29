def find():
    global total, slash, bslash, row, col
    for i in range(5):
        if row[i] == 5:
            total += 1
            row[i] = 0
        if col[i] == 5:
            total += 1
            col[i] = 0
    if bslash == 5:
        total += 1
        bslash = 0
    if slash == 5:
        total += 1
        slash = 0

chul = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
location = [[]]*26
col = [0]*5
row = [0]*5
slash = 0
bslash = 0

for i in range(5):
    for j in range(5):
        location[chul[i][j]] = [i, j]
total = 0
cnt = 0
result = False
for i in range(5):
    for j in range(5):
        cnt += 1
        r = location[mc[i][j]][0]
        c = location[mc[i][j]][1]
        row[r] += 1
        col[c] += 1
        if r + c == 4:
            bslash += 1
        if r == c:
            slash += 1
        find()
        if total >= 3:
            print(cnt)
            result = True
            break
    if result:
        break