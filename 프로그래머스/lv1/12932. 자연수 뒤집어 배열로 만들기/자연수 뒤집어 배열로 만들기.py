def solution(n):
    answer = []
    n=str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))
    answer.reverse()
    # print(answer)
    return answer