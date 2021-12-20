import sys
input = sys.stdin.readline

gathers = ['a', 'e', 'i', 'o', 'u']

def check1(word):
    for g in gathers:
        if g in word:
            return True
    return False

def check2(word):
    gather, consonant = 0, 0
    for w in word:
        if w in gathers:
            gather += 1
            consonant = 0
        else:
            gather = 0
            consonant += 1
        if gather >= 3 or consonant >=3:
            return False
    return True

def check3(word):
    for i in range(len(word)):
        if word[i:i+2] == word[i]*2:
            if word[i] == 'e' or word[i] == 'o':
                continue
            return False
    return True

while 1:
    word = input().rstrip()

    if word == 'end':
        exit()

    if not check1(word):
        print('<' + word + '> is not acceptable.')
        continue

    if not check2(word):
        print('<' + word + '> is not acceptable.')
        continue

    if not check3(word):
        print('<' + word + '> is not acceptable.')
        continue
    print('<' + word + '> is acceptable.')