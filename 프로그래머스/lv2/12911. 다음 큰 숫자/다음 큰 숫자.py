def solution(n):
    
    temp=str(bin(n))
    rule2=temp.count('1')
    # print(rule2)
    i=n
    while True:
        i+=1
        comp=str(bin(i))
        rule20=comp.count('1')
        if rule2==rule20:
            break
        
    answer = i
    return answer

print(solution(78))
print(solution(15))