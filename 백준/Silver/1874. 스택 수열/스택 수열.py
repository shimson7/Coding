'''
1
1 2
1 2 3
1 2 3 4      4 빠짐 [4]
1 2 3        3 빠짐 [4,3]
1 2
1 2 5
1 2 5 6      6 빠짐 [4,3,6]
1 2 5 7
1 2 5 7 8    8 빠짐 [4,3,6,8]
1 2 5 7      7 빠짐 [4,3,6,8,7]
1 2 5        5 빠짐 [4,3,6,8,7,5]
1 2          2 빠짐 [4,3,6,8,7,5,2]
1            1 빠짐 [4,3,6,8,7,5,2,1]
'''

n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)