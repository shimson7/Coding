while True:
    num=int(input())
    if num==0:
        break
    numCollect=[]
    for i in range(num+1):
        numCollect.append(i)
    print(sum(numCollect))