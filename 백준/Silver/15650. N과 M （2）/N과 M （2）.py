from itertools import combinations

N, M = map(int, input().split())

arr=[i for i in range(1,N+1)]

c_list=list(combinations(arr, M))

for j in range(len(c_list)):
    for k in range(len(c_list[j])):
        print(c_list[j][k], end=' ')
    print()