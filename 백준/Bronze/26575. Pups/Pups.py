T=int(input())
for _ in range(T):
    pupcollect=list(map(str, input().split()))
    pup=float(pupcollect[0])
    feed=float(pupcollect[1])
    price=float(pupcollect[2])
    cal=pup*feed*price
    print("$"+f'{cal:.2f}')