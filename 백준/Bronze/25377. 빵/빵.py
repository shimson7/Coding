inf=1000000000
ans=inf

for _ in range(int(input())):
    A, B = map(int, input().split())

    if A <= B:
        ans=min(ans, B)

if ans==inf:
    print(-1)
else:
    print(ans)