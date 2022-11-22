numberCollection=[]
maxNumber=0
line=0
indexNumber=0
for i in range(9):
    numberCollection.append(list(map(int, input().split())))

for j in range(9):
    if maxNumber<max(numberCollection[j]):
        maxNumber=max(numberCollection[j])

for k in range(9):
    if maxNumber in numberCollection[k]:
        line=k+1
        indexNumber=numberCollection[k].index(maxNumber)+1

print(maxNumber)
print(line, indexNumber)