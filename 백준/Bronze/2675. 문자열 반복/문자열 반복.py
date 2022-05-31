test=int(input())

for i in range(test):
    R, S = list(map(str,input().split()))
    R=int(R)

    for i in range(len(S)):
        print(S[i]*R, end='')
    print()
