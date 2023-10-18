def solution(num_list):
    answer = 0
    multi=1
    square=0
    for i in range(len(num_list)):
        multi*=num_list[i]
        square+=num_list[i]
    square=square**2
    if multi<square:
        answer=1
    else:
        answer=0
    return answer