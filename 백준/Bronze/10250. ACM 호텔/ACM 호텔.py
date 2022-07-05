'''
T 테스트 케이스 수
H 층
W 방 수
N 번째 손님
'''

'''
손님은 무조건 모든층 1호부터 들어감
그 다음 모든 층 2호부터 채우는 식
따라서 예제 102호에는 7번째 손님이 올것
'''
T=int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    b = N//H+1
    if a==0 :
        a=H
        b-=1
    print(a*100+b)