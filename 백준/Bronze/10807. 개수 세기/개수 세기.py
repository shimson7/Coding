N=int(input())
# num_list=[0]*N
# print(num_list)
num_list=list(map(int, input().split()))
# print(num_list)
answer=num_list.count(int(input()))
print(answer)