import sys
input=sys.stdin.readline

n=int(input())

#코드1 실행횟수 함수
def fib1(n):
    cnt = 0

    if n==1 or n==2:
        cnt+=1
        return cnt
    else:
        return (fib1(n-1)+fib1(n-2))

#코드2 실행횟수 함수
def fib2(n):
    f=[0]*(n+1)
    f[1]=1; f[2]=1
    cnt=0
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        cnt+=1
    # return f[n]
    return cnt

print(fib1(n), fib2(n))