import sys
input=sys.stdin.readline

N,K=map(int, input().split())
temper=list(map(int, input().split()))

result=[]
result.append(sum(temper[:K]))

for i in range(N-K):
    result.append(result[i] - temper[i] + temper[K+i]) # 맨 앞을 빼고 맨 뒤에 하나 추가하는 형식

print(max(result))