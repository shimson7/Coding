T=int(input())
for _ in range(T):
    C,V=map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(int(C/V), C%V))