'''
a~z까지 개수를 세서 보여줘야함
0부터 25
'''
S=input()
alphabet_list=[0]*26
for i in range(len(S)):
    answer=ord(S[i])
    #97~122 a~z
    alphabet_list[answer-97]+=1
print(*alphabet_list)