AB=input()
Acount=0
Bcount=0
for i in range(len(AB)):
    if AB[i]=="A":
        Acount+=1
    elif AB[i]=="B":
        Bcount+=1
print(Acount,":",Bcount)