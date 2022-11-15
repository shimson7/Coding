letter=input()
letter_list=[]
answer=""
for i in range(len(letter)):
    letter_list.append(letter[i])

for i in range(1,len(letter_list)+1):
    answer+=letter_list[-i]

print(answer)