max_people=0
people=0

for _ in range(4):
    O,I=map(int, input().split())
    people-=O
    people+=I
    max_people=max(max_people,people)

print(max_people)