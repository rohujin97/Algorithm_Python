S = "bbbaaaaa"
def solution(S):
    str = []

    start = 0
    while start < len(S):
        index = 1

        if start == len(S)-1:
            str.append(index)
            break
        else:
            for end in range(start+1, len(S)):
                if S[start] == S[end]:
                    index += 1
                    if end == len(S)-1:
                        start = end + 1
                else:
                    start = end
                    break
            str.append(index)

    maxS = max(str)

    total = 0
    for i in str:
        diff = maxS - i
        total += diff

    return total


print(solution(S))