def solution(num_list):
    answer = []
    if num_list[-2]<num_list[-1]:
        num_list.insert(10, num_list[-1]-num_list[-2])
    else:
        num_list.insert(10, num_list[-1]*2)
    answer=num_list
    return answer