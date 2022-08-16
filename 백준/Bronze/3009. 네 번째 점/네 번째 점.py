X = []
Y = []

for _ in range(3):
    fir,sec=map(int, input().split())
    X.append(fir)
    Y.append(sec)

# print(X)
# print(Y)

if X.count(X[0])==2:
    temp=X[0]
    X.remove(temp)
    X.remove(temp)
elif X.count(X[1])==2:
    temp = X[1]
    X.remove(temp)
    X.remove(temp)

if Y.count(Y[0])==2:
    temp = Y[0]
    Y.remove(temp)
    Y.remove(temp)
elif Y.count(Y[1])==2:
    temp = Y[1]
    Y.remove(temp)
    Y.remove(temp)

print(*X, *Y)