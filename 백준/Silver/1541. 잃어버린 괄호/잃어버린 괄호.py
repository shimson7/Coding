N=input()
M=N.split('-')

# print(M)

answer=0
# 첫번째는 -로 시작할 경우의 수가 있어서 따로 작업
x=sum(map(int, (M[0].split('+'))))
if N[0]=='-':
    answer -= x
else:
    answer += x

for x in M[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
    x=sum(map(int, (x.split('+'))))
    answer -= x
print(answer)