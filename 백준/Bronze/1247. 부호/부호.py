import sys
input=sys.stdin.readline

for i in range(3):
    N = int(input())
    num_list = []
    for j in range(N):
        num_list.append(int(input()))
    answer=sum(num_list)
    if answer>0:
        print('+')
    elif answer==0:
        print(0)
    elif answer<0:
        print('-')