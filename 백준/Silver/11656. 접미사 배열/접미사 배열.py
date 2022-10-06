S=input()

S_list=[]

for i in range(len(S)):
    answer = ''
    for j in range(i, len(S)):
        answer+=S[j]
    S_list.append(answer)

S_list.sort()

for item in S_list:
    print(item)