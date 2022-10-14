def solution(n):
    answer=''
    String_n=str(n)
    number_list=[]
    for i in range(len(String_n)):
        number_list.append(String_n[i])
    number_list.sort(reverse=True)
    for j in range(len(number_list)):
        answer+=number_list[j]
    return int(answer)