N,W,H = map(int, input().split())

for i in range(N):
    l = int(input())
    if W**2+H**2>=l**2:
        print("DA")
    else:
        print("NE")
