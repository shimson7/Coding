def prime_list(n):
    sieve = [True] * ((2*n)+1)
    m = int(n ** 0.5)
    for i in range(2, 2*m + 1):
        if sieve[i] == True:
            for j in range(2*i, (2*n)+1, i):
                sieve[j] = False

    return len([i for i in range(n+1, 2*n+1) if sieve[i] == True])

n=int(input())

while n!=0:
    print(prime_list(n))
    n=int(input())

