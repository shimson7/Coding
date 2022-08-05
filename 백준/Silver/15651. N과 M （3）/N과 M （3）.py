import itertools
from itertools import product

N, M = map(int, input().split())

arr=[i for i in range(1,N+1)]

c_list=list(itertools.product(arr, repeat=M))

for j in range(len(c_list)):
    for k in range(len(c_list[j])):
        print(c_list[j][k], end=' ')
    print()