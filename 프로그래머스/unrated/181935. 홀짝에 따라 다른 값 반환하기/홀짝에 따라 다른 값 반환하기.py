def solution(n):
    answer = 0
    if n%2==1:
        for i in range(n+1):
            if i%2==1:
                answer+=i
    elif n%2==0:
        for i in range(n + 1):
            if i % 2 == 0:
                answer+=i**2
    return answer