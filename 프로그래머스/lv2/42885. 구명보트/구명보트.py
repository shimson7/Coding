'''
40<=사람<=240
40<=무게제한<=240
한번에 최대 2명 탑승가능
구명보트 최대한 적게 사용해 모든 사람을 구출해야함
while문 사용
'''

def solution(people, limit):
    answer = 0
    
    people.sort()
    
    start, end = 0, len(people) - 1
    
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    
    return answer
