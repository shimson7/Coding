MBTI=input()
N=int(input())
cnt=0
for i in range(N):
    friend=input()
    if MBTI==friend:
        cnt+=1

print(cnt)