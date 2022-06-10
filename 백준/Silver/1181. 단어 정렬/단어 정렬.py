import sys

N=int(sys.stdin.readline())
word_list=[]

for i in range(N):
    case=input()
    word_list.append(case)
word_set=set(word_list)
word_list=list(word_set)
word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)