N = int(input())
confetti = [list(map(int, input().split())) for _ in range(N)]
paper = [[0]*100 for _ in range(100)]

for i in range(N):
    a = confetti[i][0]
    b = confetti[i][1]
    for r in range(b, b+10):
        for c in range(a, a+10):
            if paper[r][c] == 0:
                paper[r][c] = 1
total = 0
for i in range(100):
    total += sum(paper[i])
print(total)