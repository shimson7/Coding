A=int(input())
B=int(input())
time=A+B
if time>12:
    while time>12:
        time-=12
    print(time)
else:
    print(time)