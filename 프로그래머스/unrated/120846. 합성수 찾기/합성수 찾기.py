def solution(n):
    number_list=[i for i in range(1,n+1)]
    answer_list=[]
    for j in range(len(number_list)):
        count=0
        for k in range(1,n+1):
            if number_list[j]%k==0:
                count+=1
        if count>=3:
            answer_list.append(number_list[j])
    return len(answer_list)