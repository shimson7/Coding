test=int(input())

for i in range(test):
    answer=list(input())
    score = 0
    add = 0
    # 값 입력까지는 완료됨
    for i in range(len(answer)): #문자열 길이만큼 돌것
        if answer[i]=='O': # 문자가 O라면
            add+=1 # 1점 추가
            score+=add
        elif answer[i]=='X':
            add=0
    print(score)
