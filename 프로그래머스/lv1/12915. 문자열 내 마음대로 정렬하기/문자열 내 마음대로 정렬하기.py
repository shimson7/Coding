def solution(strings, n):
    answer = []
    strings=sorted(strings)
    answer=sorted(strings, key=lambda strings:strings[n])
    print(answer)
    return answer