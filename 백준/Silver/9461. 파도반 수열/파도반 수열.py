import sys
input=sys.stdin.readline

T=int(input())

#코드2 실행횟수 함수
def fx(n):
    f=[0]*101
    f[0]=0; f[1]=1; f[2]=1; f[3]=1;
    for i in range(3,n+1):
        f[i]=f[i-2]+f[i-3]
    return f[n]

for i in range(T):
    n=int(input())
    print(fx(n))