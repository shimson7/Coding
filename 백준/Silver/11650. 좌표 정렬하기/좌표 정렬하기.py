test=int(input())
test_list=[]

for i in range(test):
    A=list(map(int, input().split()))
    test_list.append(A)

test_list.sort()
for i in range(len(test_list)):
    print(test_list[i][0],test_list[i][1])