def solution(seoul):
    answer = 0
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            answer=i
            break
    answer="김서방은 "+str(i)+"에 있다"
    return answer