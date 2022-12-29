import heapq

heap=[]
N=int(input())

for i in range(N):
    numbers=map(int, input().split())
    for number in numbers:
        if len(heap)<N:
            heapq.heappush(heap, number)
        else:
            if heap[0]<number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
                
print(heap[0])