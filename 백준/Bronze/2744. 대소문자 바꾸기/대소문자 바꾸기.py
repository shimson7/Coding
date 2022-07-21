answer=input()
answer_list=[]
for i in range(len(answer)):
    # print(answer[i])
    if answer[i].isupper():
        item=answer[i].lower()
    elif answer[i].islower():
        item=answer[i].upper()
    # print(answer[i])
    answer_list.append(item)

for j in range(len(answer_list)):
    print(answer_list[j], end='')