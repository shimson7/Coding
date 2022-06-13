import sys
input=sys.stdin.readline

Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

li = list(input())
result=0

for i in li:
    for j in Number:
        if i in j :
            result += Number.index(j) + 3
    
print(result)
'''
1       2초
2=ABC   3초
3=DEF   4초
4=GHI   5초
5=JKL   6초
6=MNO   7초
7=PQRS  8초
8=TUV   9초
9=WXYZ  10초
0=operator  11초
'''