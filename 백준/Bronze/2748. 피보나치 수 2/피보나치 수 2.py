n=int(input())
numberCollection=[0]*(n+1)
numberCollection[1]=1
for i in range(2,n+1):
    numberCollection[i]=numberCollection[i-1]+numberCollection[i-2]

print(numberCollection[n])