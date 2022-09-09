while True:
    re=''
    answer=input()
    if answer=='END':
        break
    n=len(answer)
    for i in range(n-1,-1,-1):
        re+=answer[i]
    print(re)