from collections import deque

def solution(A,B):
    answer = 0
    A=sorted(A)
    B=sorted(B)
    A_list=deque(A)
    B_list=deque(B)

    while A_list:
        #A에서 최소값 뽑기
        a=A_list.popleft()
        #B에서 최대값 뽑기
        b=B_list.pop()
        #A*B 실행 answer에 더하기
        answer+=a*b
        #1회전 마무리 덱에 아무것도 없을때까지
    print(answer)
    return answer

A=[1, 4, 2]
B=[5, 4, 4]
# A=[1,2]
# B=[3,4]

solution(A,B)