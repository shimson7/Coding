people=0
big=0
for _ in range(10):
    Out,In=map(int, input().split())
    people=people+In-Out
    big=max(big, people)
print(big)