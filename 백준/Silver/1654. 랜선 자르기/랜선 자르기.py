N, K = map(int, input().split())
lan_list=[]

for i in range(N):
    lan_list.append(int(input()))

# print(lan_list)
low=1 #제일 낮은 높이
high=max(lan_list) #제일 높은 높이

while low <= high:
    mid=(low+high)//2
    cnt=0
    for j in range(len(lan_list)):
        cnt+=lan_list[j] // mid
    if cnt>=K:
        low=mid+1
    else:
        high=mid-1
print(high)
