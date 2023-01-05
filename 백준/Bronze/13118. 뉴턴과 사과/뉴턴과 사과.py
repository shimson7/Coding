people=list(map(int, input().split()))
apple=list(map(int, input().split()))

if apple[0] in people:
    print(people.index(apple[0])+1)
elif apple[0]+apple[2] in people:
    print(people.index(apple[0]+apple[2])+1)
elif apple[0]-apple[2] in people:
    print(people.index(apple[0]-apple[2])+1)
else:
    print(0)