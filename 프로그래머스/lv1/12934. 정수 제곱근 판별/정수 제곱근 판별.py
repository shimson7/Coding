import math

def solution(n):
    answer = 0
    result=math.sqrt(n)
    # print(result)
    if result.is_integer():
        answer=(int(result)+1)**2
    else:
        answer=-1
    # print(answer)
    return answer
