n=int(input())
for _ in range(n):
    g=0
    b=0
    check=''
    answer=input()
    answer2=answer.lower()
    for i in range(len(answer2)):
        if answer2[i]=='g':
            g+=1
        elif answer2[i]=='b':
            b+=1
    if g>b:
        check="GOOD"
    elif g<b:
        check="A BADDY"
    elif g==b:
        check="NEUTRAL"

    print('{} is '.format(answer)+check)