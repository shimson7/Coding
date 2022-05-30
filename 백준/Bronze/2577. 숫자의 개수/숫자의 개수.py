a=int(input())
b=int(input())
c=int(input())

math=list((str(a*b*c)))
e = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

for i in range(len(math)):
    if '0' == math[i]:
        e['0']+=1
    elif '1' == math[i]:
        e['1']+=1
    elif '2' == math[i]:
        e['2']+=1
    elif '3' == math[i]:
        e['3']+=1
    elif '4' == math[i]:
        e['4']+=1
    elif '5' == math[i]:
        e['5']+=1
    elif '6' == math[i]:
        e['6']+=1
    elif '7' == math[i]:
        e['7']+=1
    elif '8' == math[i]:
        e['8']+=1
    elif '9' == math[i]:
        e['9']+=1

answer=list(e.values())
for i in range(len(e)):
    print(answer[i])