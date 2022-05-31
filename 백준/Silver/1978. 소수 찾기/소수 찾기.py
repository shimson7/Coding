test=int(input())

number=list(map(int, input().split()))
answer=[]

for i in range(len(number)):
    cnt=0
    for j in range(1,1001):
        if number[i] % j == 0:
            cnt+=1
    if cnt==2:
        answer.append(number[i])
print(len(answer))
