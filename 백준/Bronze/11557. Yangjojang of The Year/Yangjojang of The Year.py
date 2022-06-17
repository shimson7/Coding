for i in range(int(input())):
    name=''
    max=0
    for i in range(int(input())):
        schoolname,drink=input().split()
        drink=int(drink)
        if drink > max:
            name=schoolname
            max=drink
    print(name)