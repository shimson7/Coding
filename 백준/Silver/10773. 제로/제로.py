K=int(input())
list=[]

for i in range(K):
    case=int(input())
    if case==0 and len(list)!=0:
        list.pop()
    else:
        list.append(case)
print(sum(list))