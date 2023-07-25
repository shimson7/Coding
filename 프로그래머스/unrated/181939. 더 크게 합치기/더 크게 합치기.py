def solution(a, b):
    left=str(a)+str(b)
    right=str(b)+str(a)
    if int(left)>int(right):
        answer = int(left)
    else:
        answer = int(right)
    return answer