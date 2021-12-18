import sys
input = sys.stdin.readline

def check(chul):
    global count
    dialog, b_dialog = 0, 0

    for i in range(5):
        if str(chul[i]).count('[0, 0, 0, 0, 0]') and not visited_row[i]:
            count += 1
            visited_row[i] = True

        col = list(map(lambda x:x[i], chul))
        if str(col).count('[0, 0, 0, 0, 0]') and not visited_col[i]:
            count += 1
            visited_col[i] = True
        dialog += chul[i][i]
        b_dialog += chul[i][4-i]

    if dialog == 0 and not visited_dialog[0]:
        count += 1
        visited_dialog[0] = True

    if b_dialog == 0 and not visited_dialog[1]:
        count += 1
        visited_dialog[1] = True

    return count

count, order = 0, 0
visited_row, visited_col, visited_dialog = [False]*5, [False]*5, [False]*2
chul = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

for num in range(25):
    for i in range(5):
        for j in range(5):
            if mc[num] == chul[i][j]:
                chul[i][j] = 0
                check(chul)
                order += 1
                if count >= 3:
                    print(order)
                    exit()