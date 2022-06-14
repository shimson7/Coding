#첫째줄에 회원수 N이 주어진다.
N=int(input())
membership=[[0,'']]*N


#회원 정보 입력
for i in range(N):
    #membership.append(input().split())
    age,name=input().split()
    age=int(age)
    membership[i]=age,name

#나이를 우선 비교해서 나이가 적은순으로 앞 배치
membership.sort(key=lambda x:x[0])

for i in range(N):
    print(membership[i][0], membership[i][1])