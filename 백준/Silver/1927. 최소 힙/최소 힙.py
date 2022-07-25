import sys
import heapq

input=sys.stdin.readline
N=int(input())
number_list=[]
heapq.heapify(number_list)

for i in range(N):
    number=int(input())
    if number!=0:
        heapq.heappush(number_list, number)
    elif number==0:
        if len(number_list)==0:
            print(0)
            continue
        print(heapq.heappop(number_list))
