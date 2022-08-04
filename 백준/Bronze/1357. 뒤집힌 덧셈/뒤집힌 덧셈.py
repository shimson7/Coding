def Rev(n):
    number_list=[]
    number=''
    for i in range(len(n)):
        number_list.append(n[i])
    number_list.reverse()
    for i in range(len(n)):
        number+=number_list[i]
    answer=int(number)
    return answer


X, Y = input().split()
A=Rev(X)
B=Rev(Y)
correct=Rev(str(A+B))
print(correct)