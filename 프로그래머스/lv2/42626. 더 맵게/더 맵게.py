from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        n1=heappop(scoville)  # 사용한 가장 맵지 않은 음식 제거
        n2=heappop(scoville)  # 사용한 두번째로 맵지 않은 음식 제거
        new_food = n1 + (n2 * 2)  # 새로운 음식을 만들었음
        heappush(scoville, new_food) # 새로운 음식을 리스트에 추가함
        answer += 1
    return answer if scoville[0] >= K else -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))