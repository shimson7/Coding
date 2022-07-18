import sys
input=sys.stdin.readline
N,K=map(int, input().split())

answer=0
coin_list=[]
for i in range(N):
    coin=int(input())
    if coin>K:
        continue
    else:
        coin_list.append(coin)

# print(coin_list)

share=K//coin_list[-1] #몫 4
remain=K%coin_list[-1] #나머지 200

answer+=share
while True:
    if remain==0:
        break
    coin_list.pop()
    share=remain//coin_list[-1]
    remain=remain%coin_list[-1]
    answer+=share
print(answer)
'''
K보다 큰 돈은 볼 필요 없음

K보다 금액 작은것으로 나누고 몫 구하기
금액중 가장 큰것으로 나누고, 나머지에 대해서 다시 진행 이때 나머지도 마찬가지로
나머지보다 큰 금액 무시하고 가장 큰 금액으로 나누기 실행  

'''