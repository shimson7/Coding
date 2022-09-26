N=int(input())
rope=[]
value=[]
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for num in range(N):
    value.append(rope[num]*(num+1))
print(max(value))