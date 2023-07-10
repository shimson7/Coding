numList = list(map(int, input().split()))

numList.sort()

d=min(numList[1]-numList[0], numList[2]-numList[1])

for i in range(len(numList)):
    temp = numList[i]
    
    if temp+d not in numList:
        print(temp+d)
        break