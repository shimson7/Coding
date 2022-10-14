def solution(phone_number):
    answer=''
    count=4
    for i in range(len(phone_number)):
        if i==len(phone_number)-count:
            answer+=phone_number[i]
            count-=1
        else:
            answer+='*'
    return answer