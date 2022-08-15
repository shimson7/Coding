import sys
input=sys.stdin.readline

T=int(input())
input()
for _ in range(T):
    N=int(input())
    candy_list=[]
    for i in range(N):
        candy_list.append(int(input()))
    answer=sum(candy_list)%N
    # print(answer)
    if answer==0:
        print("YES")
    else:
        print("NO")
    input()