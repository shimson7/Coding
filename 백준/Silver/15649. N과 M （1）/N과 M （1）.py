from itertools import permutations

N, M = map(int, input().split())

arr=[i for i in range(1,N+1)]

p_list=list(permutations(arr, M))

for j in range(len(p_list)):
    for k in range(len(p_list[j])):
        print(p_list[j][k], end=' ')
    print()