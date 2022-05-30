a=list(map(int, input().split()))
list=[1,2,3,4,5,6,7,8]

#print(a)
if a == list:
     print('ascending')
elif a == list[::-1]:
    print('descending')
else:
    print('mixed')