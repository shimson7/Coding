ABCD=list(map(int, input().split()))
ABCD.sort()
print(ABCD[-2]*min(ABCD))