N=input()

answer=list(N)
answer.sort(reverse=True)

for i in range(len(answer)):
    print(answer[i], end='')