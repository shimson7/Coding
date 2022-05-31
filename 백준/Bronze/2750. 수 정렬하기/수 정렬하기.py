test=int(input())
number_list=[]
for i in range(test):
    number=int(input())
    number_list.append(number)

number_list.sort()
for i in range(len(number_list)):
    print(number_list[i])