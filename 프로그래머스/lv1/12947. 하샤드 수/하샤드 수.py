def solution(x):
    answer = ''
    plus=0
    num_list=[]
    # 수를 나눠서 형변환하여 리스트로 넣어줌
    for i in range(len(str(x))):
        num_list.append(str(x)[i])
    # print(num_list)
    # 나눈 수를 형변환하여 더해줌
    for i in range(len(num_list)):
        plus+=int(num_list[i])
    # print(plus)
    if x % plus == 0:
        answer=True
    else:
        answer=False
    print(answer)
    return answer