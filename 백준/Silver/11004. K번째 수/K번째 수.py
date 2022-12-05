N, K = map(int, input().split())
numberCollect=list(map(int, input().split()))
numberCollect.sort()
print(numberCollect[K-1])
