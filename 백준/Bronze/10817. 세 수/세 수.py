test=list(map(int, input().split()))
test.remove(max(test))
test.remove(min(test))
answer=test[0]
print(answer)