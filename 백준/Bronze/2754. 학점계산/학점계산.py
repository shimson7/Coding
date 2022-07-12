'''
A+: 4.3, A0: 4.0, A-: 3.7

B+: 3.3, B0: 3.0, B-: 2.7

C+: 2.3, C0: 2.0, C-: 1.7

D+: 1.3, D0: 1.0, D-: 0.7

F: 0.0
'''
grade=input()
g_list=[]
for i in range(len(grade)):
    g_list.append(grade[i])
# print(g_list)
if g_list[0]=='A':
    if g_list[1]=='+':
        print(4.3)
    elif g_list[1]=='0':
        print(4.0)
    elif g_list[1]=='-':
        print(3.7)
elif g_list[0]=='B':
    if g_list[1]=='+':
        print(3.3)
    elif g_list[1]=='0':
        print(3.0)
    elif g_list[1]=='-':
        print(2.7)
elif g_list[0] == 'C':
    if g_list[1]=='+':
        print(2.3)
    elif g_list[1]=='0':
        print(2.0)
    elif g_list[1]=='-':
        print(1.7)
elif g_list[0] == 'D':
    if g_list[1]=='+':
        print(1.3)
    elif g_list[1]=='0':
        print(1.0)
    elif g_list[1]=='-':
        print(0.7)
elif g_list[0] == 'F':
    print(0.0)