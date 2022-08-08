import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
num_list=[]
num_list=deque(num_list)

for i in range(N):
    order=input().split()
    if order[0]=='push':
        num_list.append(order[1])

    elif order[0]=='pop':
        if len(num_list)==0:
            print(-1)
        else:
            print(num_list.popleft())

    elif order[0]=='size':
        print(len(num_list))

    elif order[0]=='empty':
        if len(num_list)!=0:
            print(0)
        else:
            print(1)

    elif order[0]=='front':
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[0])

    elif order[0]=='back':
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[-1])