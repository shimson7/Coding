numberCollection = list(map(int, input().split()))
first=max(numberCollection)

numberCollection.remove(first)
second=max(numberCollection)

print(first+second)