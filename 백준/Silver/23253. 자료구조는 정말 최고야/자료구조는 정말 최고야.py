import sys
input=sys.stdin.readline

N, M=map(int, input().split())

f = True
for _ in range(M):
    i=int(input())
    k=list(map(int, input().split()))
    for j in range(i-1):
        if k[j] <k[j+1]:
            f = False
            break
    if not f:break

print('Yes' if f else 'No')