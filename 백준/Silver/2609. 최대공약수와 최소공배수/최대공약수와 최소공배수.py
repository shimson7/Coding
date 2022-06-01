import math

def solution(n,m):
    a=math.gcd(n,m) # 최대공약수
    b=(n * m) // math.gcd(n,m) # 최소공배수
    print(a)
    print(b)

i,j=map(int, input().split())
solution(i,j)