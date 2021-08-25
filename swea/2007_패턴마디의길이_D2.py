T = int(input())
for test_case in range(1, T+1):
    st = input()
    madi = st[0]
    cur = st[0]
    for i in range(1, len(st)):
        if st[i] != cur: # 일치하지 않는다면
            madi += st[i]
        else: # 일치한다면 마디 동일한지 확인
            if madi == st[i:i+len(madi)]:
                print("#%d %d" %(test_case, len(madi)))
                break
            madi += st[i:len(madi)+1]

