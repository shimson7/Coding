N=int(input())
for _ in range(N):
    answer=input()
    if 6<=len(answer) and len(answer)<=9:
        print("yes")
    else:
        print("no")