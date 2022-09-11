
grade_list={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

grade_total=0
hakjum_total=0

for _ in range(20):
    name,hakjum,grade=input().split()
    if grade in grade_list:
        point=float(hakjum)*grade_list[grade]
    elif grade=='P':
        continue
    grade_total+=point
    hakjum_total+=float(hakjum)

print(grade_total/hakjum_total)