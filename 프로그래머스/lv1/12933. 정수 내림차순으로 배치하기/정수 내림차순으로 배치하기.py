def solution(n):
    n_list=[]
    answer=''
    n=str(n)
    for i in range(len(n)):
        n_list.append(n[i])
    n_list.sort(reverse=True)
    for j in range(len(n_list)):
        answer+=str(n_list[j])
    return int(answer)