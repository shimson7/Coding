from collections import deque

N=int(input())
A=list(map(int, input().split()))
A=sorted(A)
A=deque(A)
B=list(map(int, input().split()))
B=sorted(B)
B=deque(B)

answer=0
for _ in range(N):
    a=A.popleft()
    b=B.pop()
    answer+=a*b

print(answer)