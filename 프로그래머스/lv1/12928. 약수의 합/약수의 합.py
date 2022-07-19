def solution(n):
    num_list=[]
    for i in range(1,n+1):
        if n%i==0:
            num_list.append(i)
    answer=sum(num_list)
    print(answer)
    return answer