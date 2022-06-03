from functools import lru_cache

@lru_cache(maxsize=None)
def pib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return pib(n-1)+pib(n-2)

answer=int(input())
print(pib(answer))