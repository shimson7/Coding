import math

M = list(map(int, input().split()))
total=0

for i in range(len(M)):
    total+=math.pow(M[i], 2)

total%10

print(int(total%10))