# 부분수열의 합 - 백준
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(idx, hap): #itertools 사용보다 재귀가 더 빠름
    global cnt
    if idx == n:
        return
    hap += arr[idx] # hap이 m과 같은지 확인전에 더해야 마지막 수까지 더할 수 있음
    if hap == m:
        cnt += 1
    dfs(idx+1, hap - arr[idx])
    dfs(idx+1, hap)
    
cnt = 0
dfs(0, 0)

print(cnt)