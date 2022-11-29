T = int(input())
for i in range(T):
    numberCollection=list(map(int, input().split()))
    numberCollection.sort()
    print(numberCollection[-3])