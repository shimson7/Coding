'''

'''
N=int(input())
table=[]
for _ in range(N):
    stu_info=list(map(str, input().split()))
    table.append(stu_info)

#입력이 마무리 되었으므로 정렬
table.sort(key=lambda x: (-int(x[1]),int(x[2]), -int(x[3]), x[0]))

for student in table:
    print(str(student[0]))