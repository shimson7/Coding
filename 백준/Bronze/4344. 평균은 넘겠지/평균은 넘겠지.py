#1. 테스트 케이스 입력
test=int(input())

for i in range(test): # 테스트 케이스만큼 반복
    avg=0 #테스트케이스가 끝나면 0으로 초기화해줘야함
    cnt=0 #평균이 넘는 학생 수
    # 2. 학생의 수 입력, 학생 수만큼 점수 입력
    score_list = list(map(int, input().split()))
    '''첫번째 자리에는 학생 수가 들어가고 두번째부터 성적이 입력될거라 첫번째 제외해야함'''
    avg = (sum(score_list)-score_list[0]) / score_list[0] #첫번째 학생 수를 빼줬음
    for j in range(len(score_list)):
        if j==0:
            continue
        if score_list[j]>avg: #성적이 평균보다 클때
            cnt+=1
    answer=round((cnt/score_list[0])*100, 3)
    # 3. 한줄씩 평균을 넘는 학생들 비율 반올림하여 소수점 셋째 자리까지 출력
    print('{:.3f}%'.format(answer))
