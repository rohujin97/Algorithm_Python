import sys
input = sys.stdin.readline

dr = [1, 0, 1, -1]
dc = [0, 1, 1, 1]

def omoc(start, cur, cnt):
    r, c, color, k = cur
    if cnt == 5:
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 > nr or nr >= 19 or 0 > nc or nc >= 19 or baduk[nr][nc] != color:
            result[color].append(start)
        return
    nr = r + dr[k]
    nc = c + dc[k]
    if 0 <= nr < 19 and 0 <= nc < 19:
        if baduk[nr][nc] == color:
            omoc(start, [nr, nc, color, k], cnt + 1)



result = [[] for _ in range(3)]
baduk = [list(map(int, input().split())) for _ in range(19)]

for r in range(19):
    for c in range(19):
        color = baduk[r][c]
        if color != 0:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                br = r - dr[k]
                bc = c - dc[k]
                if 0 > nr or nr >= 19 or 0 > nc or nc >= 19 or baduk[nr][nc] != color: continue
                if 0 > br or br >= 19 or 0 > bc or bc >= 19 or baduk[br][bc] != color:
                    omoc([r, c], [nr, nc, color, k], 2)
black = result[1]
white = result[2]

if len(black) == 1 and (len(white) == 0 or len(white) > 1):
    print(1)
    print(black[0][0]+1, black[0][1]+1)
elif (len(black) == 0 or len(black) > 1) and len(white) == 1:
    print(2)
    print(white[0][0]+1, white[0][1]+1)
else:
    print(0)