import math

N=int(input())

ring_list=list(map(int, input().split()))

for i in range(N):
    if i==0:
        continue
    GCD=math.gcd(ring_list[0],ring_list[i])
    print('{0}/{1}'.format(int(ring_list[0]/GCD),int(ring_list[i]/GCD)))
    # print(int(ring_list[0]/GCD),'/',int(ring_list[i]/GCD))