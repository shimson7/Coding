X=int(input())
N=int(input())
number_list=[]
for i in range(N):
    a,b=map(int, input().split())
    number_list.append(a*b)


if sum(number_list)==X:
    print('Yes')
else:
    print('No')