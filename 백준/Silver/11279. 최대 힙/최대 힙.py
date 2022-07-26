import sys
import heapq as hq

input=sys.stdin.readline

N=int(input())

number_list=[]
hq.heapify(number_list)

for i in range(N):
    x=int(input())
    if x==0:
        if len(number_list)==0:
            print(0)
        else:
            print(hq.heappop(number_list)*(-1)) #제일 큰 수 제거
    elif x!=0:
        hq.heappush(number_list, -x) # 힙에 숫자 추가