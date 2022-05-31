question=list(map(str, input().split()))
reverse_a=''
reverse_b=''

for a in question[0]:
    reverse_a = a + reverse_a
for b in question[1]:
    reverse_b = b + reverse_b

if int(reverse_a)>int(reverse_b):
    print(reverse_a)
else:
    print(reverse_b)
