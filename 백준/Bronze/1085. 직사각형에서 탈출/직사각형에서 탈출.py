x,y,w,h=map(int, input().split())

xmin=0
ymin=0
#c compare
c1=x-0
c2=w-x
c3=y-0
c4=h-y
#x축끼리
if c2<c1:
    xmin=c2
elif c1==c2:
    xmin=c1
elif c1<c2:
    xmin=c1
#y축끼리
if c3<c4:
    ymin=c3
elif c3==c4:
    ymin=c3
elif c4<c3:
    ymin=c4

# print(c1)
# print(c2)
# print(c3)
# print(c4)

if xmin<ymin:
    print(xmin)
elif xmin==ymin:
    print(xmin)
elif ymin<xmin:
    print(ymin)

'''
x축끼리 비교

y축끼리 비교
'''
