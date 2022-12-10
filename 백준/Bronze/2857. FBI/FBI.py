agentList=[]
cnt=0

for _ in range(5):
    agentList.append(input())

for i in range(5):
    if "FBI" in agentList[i]:
        cnt+=1
        print(i+1, end=" ")
if cnt==0:
    print("HE GOT AWAY!")