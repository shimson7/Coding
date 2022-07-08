from itertools import *

N, M = map(int, input().split())
card_list=list(map(int, input().split()))

per=list(permutations(card_list, 3)) # 3장의 조합

high=0

for i in range(len(per)):
    answer=sum(per[i])
    if answer<=M:
        if high>answer:
            continue
        high=answer
print(high)