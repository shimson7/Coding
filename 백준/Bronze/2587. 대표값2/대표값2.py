numberCollect=[]

for _ in range(5):
    number=int(input())
    numberCollect.append(number)
numberCollect.sort()

print(int(sum(numberCollect)/5))
print(numberCollect[2])