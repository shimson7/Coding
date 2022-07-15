import sys
input=sys.stdin.readline

N,M=map(int, input().split())

board=[]

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    temp=list(map(int, input().split()))
    
    for j in range(M):
        board[i][j]+=temp[j]
        
for i in range(N):
    for j in range(M):
        print(board[i][j], end=" ")
    print()