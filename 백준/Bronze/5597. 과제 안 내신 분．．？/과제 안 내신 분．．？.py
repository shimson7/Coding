stu_list=[i for i in range(1,31)]
hw_list=[]

for i in range(28):
    stu=int(input())
    hw_list.append(stu)

answer=list(set(stu_list)-set(hw_list))
answer=sorted(answer)

for j in range(len(answer)):
    print(answer[j])