N=input()
letter_list=[]
letter=''

for i in range(1,len(N)+1):
    letter+=N[i-1]
    if i%10==0:
        letter_list.append(letter)
        letter=''
    elif i==len(N):
        letter_list.append(letter)

for j in range(len(letter_list)):
    print(letter_list[j])