N=int(input())
num_list=list(map(int, input().split()))

max_num=max(num_list)
min_num=min(num_list)

print(max_num*min_num)