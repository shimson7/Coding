def solution(x):
    hashad=str(x)
    plus=0
    for i in range(len(hashad)):
        plus+=int(hashad[i])
    if x%plus==0:
        answer = True
    else:
        answer = False
    return answer