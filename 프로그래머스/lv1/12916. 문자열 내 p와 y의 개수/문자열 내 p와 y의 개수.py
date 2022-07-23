def solution(s):
    answer=''
    s=s.lower()
    a=s.count("p")
    b=s.count("y")
    if a==b:
        answer=True
    elif a!=b:
        answer=False
    return answer