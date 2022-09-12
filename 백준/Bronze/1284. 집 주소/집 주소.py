'''
0 : 4cm
1 : 2cm
~9 : 3cm
경계 1cm (전체 길이 -1)
양 끝 1cm
'''


while True:
    length=0
    answer=input()
    if answer=='0':
        break
    number_list=[]
    for i in range(len(answer)):
        number_list.append(answer[i])

    for j in range(len(number_list)):
        if number_list[j]=='0':
            length+=4
        elif number_list[j]=='1':
            length+=2
        else:
            length+=3

    #경계 (전체 길이 -1)
    length+=len(number_list)-1

    #양 끝
    length+=2
    print(length)