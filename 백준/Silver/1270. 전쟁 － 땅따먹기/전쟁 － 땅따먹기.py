N = int(input())
for i in range(N):
    a = list(map(int,input().split()))
    c= a[0]
    a = a[1:]
    b= {}
    d = True
    for j in a:
        try:
            b[j] = b[j]+1
            if(b[j] > c/2 ):
                print(j)
                d= False
                break
        except:
            b[j] = 1
    if(d):
        print('SYJKGW')