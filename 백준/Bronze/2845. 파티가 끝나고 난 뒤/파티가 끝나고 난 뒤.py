L,P = map(int, input().split())
numbers = list(map(int, input().split()))
for number in numbers:
    print((L*P-number)*-1, end=" ")
