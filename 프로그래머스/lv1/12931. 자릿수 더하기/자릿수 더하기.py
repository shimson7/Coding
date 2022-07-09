def solution(n):
    num_list=[]
    n=str(n)
    for i in range(len(n)):
        num_list.append(n[i])
    plus=0
    for i in range(len(num_list)):
        plus+=int(num_list[i])
    # print(plus)
    answer=plus
    return answer