T=int(input())

DP=[1,2,4,0,0,0,0,0,0,0]

# 한번만 실행하면 되는 친구
for i in range(3, 10):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]

for _ in range(T):
    n=int(input())
    print(DP[n-1])
