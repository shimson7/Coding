N=int(input())
people_list=[]
for i in range(N):
    people_list.append(list(map(int, input().split())))
# print(people_list)
'''입력 완료'''
rank=1
for i in range(N):
    cnt=0
    for j in range(N):
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            cnt += 1
    print(rank+cnt,end=' ')