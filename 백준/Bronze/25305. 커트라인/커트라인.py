N,k=map(int, input().split())
score=list(map(int, input().split()))
prize=[]

for i in range(k):
    prize.append(max(score))
    score.remove(max(score))

print(min(prize))