N=int(input())
cnt=0
num=1

while True:
    if '666' in str(num): #'666'을 만나면
        cnt=cnt+1 # 카운트해준다
    if cnt==N: # N만큼 카운트 되었을때
        print(num) # 해당 숫자를 출력해준다
        break

    num=num+1