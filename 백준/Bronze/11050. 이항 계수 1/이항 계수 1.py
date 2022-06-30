"""
이항 계수
n!//k!(n-k!)
"""

N,K=map(int, input().split())
za=1
mo=1
mo2=1
for i in range(1,N+1):
    za=i*za

for i in range(1,K+1):
    mo=i*mo

for i in range(1,N-K+1):
    mo2=i*mo2

# print(za)
# print(mo)
# print(mo2)
#정상 출력 완료
print(za//(mo*mo2))