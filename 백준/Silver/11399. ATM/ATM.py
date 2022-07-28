from collections import deque

N=int(input())
time_list=list(map(int, input().split()))
tmp=deque(time_list)
spendtime=[]

time=0
for i in range(len(time_list)): # 리스트를 전부 돌아봄
    #최소값을 찾아내서 spendtime에 추가
    for j in range(len(time_list)):
        if len(tmp)==0:
            break
        if time_list[j]==min(tmp):
            time += time_list[j]
            spendtime.append(time)
            tmp.remove(time_list[j])
            # print(time_list[j])

print(sum(spendtime))
