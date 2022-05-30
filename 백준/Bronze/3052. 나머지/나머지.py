set = set()

for i in range(10):
    a=int(input())
    remain=a%42
    set.add(remain)

print(len(set))