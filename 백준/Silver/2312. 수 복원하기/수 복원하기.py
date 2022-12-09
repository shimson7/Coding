def factorization(x):
    d = 2
    numberCollect=[]
    while d <= x:
        if x % d == 0:
            numberCollect.append(d)
            x = x / d
        else:
            d = d + 1
    return numberCollect

T=int(input())
for _ in range(T):
    N=int(input())
    numbers=factorization(N)
    numbers2=sorted(list(set(numbers)))
    for i in range(len(numbers2)):
        print(numbers2[i], numbers.count(numbers2[i]))