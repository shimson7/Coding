i=1

while True:
    num_list=list(map(int, input().split()))
    if num_list[0]==0 and len(num_list)==1:
        break
    print("Case "+str(i)+": Sorting... done!")
    i+=1