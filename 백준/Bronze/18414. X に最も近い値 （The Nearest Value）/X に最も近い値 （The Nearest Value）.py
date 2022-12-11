X, L, R = map(int, input().split())
res = 0
m = 100000
for n in range(L, R+1):
    if abs(X-n) < m:
        m = abs(X-n)
        res = n
print(res)