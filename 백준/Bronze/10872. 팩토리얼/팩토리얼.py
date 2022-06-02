N=int(input())
answer=1
if N==0:
    print(1)
else:
    for i in range(1,N+1):
        answer=answer*i
    print(answer)