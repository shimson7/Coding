X = input()
cnt = 0
def f(a):
    global cnt
    if len(a) == 1:
        if int(a) % 3 == 0:
            print(cnt)
            print('YES')
            return
        else:
            print(cnt)
            print('NO')
            return
    else:
        t = 0
        for i in range(len(a)):
            t += int(a[i])
        a = str(t)
        cnt += 1
        f(a)
f(X)