L=int(input())
mog=L//5
namoji=L%5

if namoji!=0:
    mog+=1

print(mog)