question=list(map(int, input().split()))
chess=[1, 1, 2, 2, 2, 8]
answer=[]
for i in range(len(chess)):
    answer.append(chess[i]-question[i])

print(* answer)