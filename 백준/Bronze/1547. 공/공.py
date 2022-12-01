M=int(input())
cupCollect=['1','2','3']
for _ in range(M):
    X, Y=map(str, input().split())
    idx_X,idx_Y= cupCollect.index(X), cupCollect.index(Y)
    cupCollect[idx_X],cupCollect[idx_Y] = cupCollect[idx_Y],cupCollect[idx_X]
print(cupCollect[0])