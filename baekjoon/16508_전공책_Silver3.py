import sys
input = sys.stdin.readline

def find(want, word, coin):
    cnt = 0
    for w in word:
        if w in want:
            cnt += 1
            want = want.replace(w, ' ', 1)
        if cnt == len(T):
            return coin
    return 987654321

T = input().rstrip()
N = int(input())
coins = [0]*N
words = [0]*N

for i in range(N):
    coin, word = map(str, input().split())
    coins[i] = int(coin)
    words[i] = word.rstrip()

result = []
for i in range(1 << N):
    new_word = ''
    sum_coin = 0
    for j in range(N):
        if (i & 1 << j) != 0:
            new_word += words[j]
            sum_coin += coins[j]
    result.append(find(T, new_word, sum_coin))

minC = min(result)
if minC == 987654321:
    print(-1)
else:
    print(minC)