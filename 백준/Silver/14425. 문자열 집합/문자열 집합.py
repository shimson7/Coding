answerCollect=[]
N, M = map(int, input().split())
cnt=0

for _ in range(N):
    answer=input()
    answerCollect.append(answer)

for _ in range(M):
    sentence=input()
    if sentence in answerCollect:
        cnt+=1

print(cnt)